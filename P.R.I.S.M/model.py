import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sentence_transformers import SentenceTransformer
import chromadb

# ==========================================
# ENGINE 1: FAKE REVIEW CLASSIFIER
# ==========================================
class ReviewAnalyzer:
    def __init__(self):
        # We build a pipeline: 
        # 1. Convert words to numbers (TF-IDF)
        # 2. Run those numbers through a probability model (Naive Bayes)
        self.model = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())
        self.is_trained = False

    def train(self, df):
        """Trains the model on our dataset."""
        # X is the review text, y is the label (0 for Real, 1 for Fake)
        X = df['ReviewText'].fillna("")
        y = df['Is_Fake']
        
        self.model.fit(X, y)
        self.is_trained = True
        print("✅ Review Classifier trained successfully.")

    def analyze(self, review_text):
        """Returns the probability that a review is genuine."""
        if not self.is_trained:
            return 0.0
            
        # predict_proba returns [Probability of 0 (Real), Probability of 1 (Fake)]
        probabilities = self.model.predict_proba([review_text])[0]
        
        # We want the probability of it being Real (index 0), converted to a percentage
        genuine_score = round(probabilities[0] * 100, 1)
        return genuine_score


# ==========================================
# ENGINE 2: SEMANTIC SEARCH
# ==========================================
class SemanticSearcher:
    def __init__(self):
        # Load a lightweight, highly efficient embedding model from Hugging Face
        print("Loading embedding model (this takes a few seconds the first time)...")
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize an in-memory Chroma database
        self.chroma_client = chromadb.Client()
        # Create a "collection" (think of it like a table in a database)
        self.collection = self.chroma_client.create_collection(name="prism_products")
        self.is_indexed = False

    def build_database(self, df):
        """Converts product descriptions into vectors and stores them."""
        # Convert descriptions to a list
        descriptions = df['Description'].fillna("").tolist()
        ids = df['ProductID'].astype(str).tolist()
        
        # Generate the mathematical vectors (embeddings)
        print("Generating product embeddings...")
        embeddings = self.encoder.encode(descriptions).tolist()
        
        # Store them in ChromaDB
        self.collection.add(
            embeddings=embeddings,
            documents=descriptions,
            ids=ids
        )
        self.is_indexed = True
        print("✅ Semantic vector database built successfully.")

    def search(self, query, df, top_k=2):
        """Searches the vector database for the closest semantic matches."""
        if not self.is_indexed:
            return pd.DataFrame()

        # Convert the user's search query into a vector
        query_embedding = self.encoder.encode([query]).tolist()
        
        # Ask ChromaDB to find the nearest neighbor vectors
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )
        
        # Extract the matching ProductIDs
        matched_ids = results['ids'][0]
        
        # Filter our original dataframe to only return those matching products
        # and ensure they stay in the exact order of relevance returned by ChromaDB
        matched_df = df[df['ProductID'].astype(str).isin(matched_ids)]
        matched_df.index = pd.Categorical(matched_df['ProductID'].astype(str), categories=matched_ids, ordered=True)
        matched_df = matched_df.sort_index()
        
        return matched_df
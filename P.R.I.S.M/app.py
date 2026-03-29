import streamlit as st
import pandas as pd
from model import ReviewAnalyzer, SemanticSearcher

# ==========================================
# 1. AI ENGINE INITIALIZATION & CACHING
# ==========================================
@st.cache_resource(show_spinner=False)
def load_ai_engines():
    """Loads the database and trains the models only ONCE per session."""
    try:
        df = pd.read_csv("products.csv")
    except FileNotFoundError:
        st.error("Database not found! Please run 'python data_prep.py' first.")
        st.stop()
        
    analyzer = ReviewAnalyzer()
    analyzer.train(df)
    
    searcher = SemanticSearcher()
    searcher.build_database(df)
    
    return analyzer, searcher, df

# ==========================================
# 2. UI LAYOUT & CONFIGURATION
# ==========================================
st.set_page_config(page_title="P.R.I.S.M. Marketplace", page_icon="🛒", layout="wide")

# Load the AI engines in the background
analyzer, searcher, product_db = load_ai_engines()

st.title("P.R.I.S.M. 🛒")
st.subheader("Product Review Intelligence & Semantic Matching")

with st.sidebar:
    st.header("About P.R.I.S.M.")
    st.write("An AI-powered MVP built to eliminate e-commerce friction.")
    st.markdown("---")
    st.write("**Core Engine:**")
    st.write("🧠 **Semantic Search:** Understands user intent in layman's terms using vector embeddings.")
    st.write("🛡️ **Review Intelligence:** Detects AI-generated and fake reviews using NLP classification.")

# ==========================================
# 3. SEARCH EXECUTION LOGIC
# ==========================================
st.markdown("### What are you looking for today?")
search_query = st.text_input(
    "Search Input", 
    label_visibility="collapsed", 
    placeholder="e.g., something to keep my coffee hot..."
)

if st.button("Search", type="primary"):
    if search_query:
        with st.spinner("Analyzing intent and searching catalog..."):
            
            # 1. Ask the Semantic Searcher for the top 2 matching products
            results_df = searcher.search(search_query, product_db, top_k=2)
            
            st.success(f"Top semantic matches for: '{search_query}'")
            
            # 2. Display the results dynamically
            cols = st.columns(2)
            
            # Iterate through the matched products and put them in columns
            for index, row in enumerate(results_df.itertuples()):
                
                # Alternate between column 1 and column 2
                col = cols[index % 2] 
                
                with col:
                    with st.container(border=True):
                        st.markdown(f"#### {row.ProductName}")
                        st.markdown(f"**Best Price:** {row.Price}")
                        st.write(f"*{row.Description}*")
                        st.divider()
                        
                        st.markdown(f"**Top Review:** '{row.ReviewText}'")
                        
                        # 3. Pass the review text to the AI Classifier
                        auth_score = analyzer.analyze(row.ReviewText)
                        
                        # 4. Logic to display green for genuine, red for fake
                        if auth_score > 60.0:
                            st.markdown(f":green[🛡️ Review Authenticity: {auth_score}% (Genuine)]")
                        else:
                            st.markdown(f":red[⚠️ Review Authenticity: {auth_score}% (Likely AI-Generated)]")
                            
                        st.button("View Deal", key=f"btn_{row.ProductID}")
    else:
        st.warning("Please enter a search term.")
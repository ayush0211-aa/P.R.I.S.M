# P.R.I.S.M

Product Review Intelligence & Semantic Matching

Overview

P.R.I.S.M. is an AI-powered e-commerce marketplace MVP built as a capstone project. It tackles two major points of friction in modern online shopping: the overwhelming presence of fake/bot-generated reviews and the rigid, keyword-dependent nature of traditional search bars.

By leveraging Machine Learning (ML) and Natural Language Processing (NLP), this project creates a smarter, safer, and more intuitive shopping experience.

🚀 Core Features

Semantic "Layman" Search: Instead of relying on exact keyword matches, P.R.I.S.M. uses vector embeddings to understand the intent behind a user's search. A user can type "something to keep my coffee hot on my desk," and the engine will return mug warmers and insulated thermoses based on semantic meaning.

Fake Review Detection: Integrates a trained classification model that analyzes the text of product reviews. It flags suspicious, repetitive, or bot-like language, providing a "Genuine" or "AI-Generated" probability score to help users make informed purchasing decisions.

Smart Pricing Engine: Displays the most relevant items sorted by the best pricing available in the database, prioritizing highly-rated, authentic products.

🛠️ Technology Stack

This project is built entirely in Python, utilizing the following libraries:

Frontend / UI: streamlit (For rapid, interactive web application deployment)

Data Manipulation: pandas (For cleaning and structuring the product/review datasets)

Machine Learning (Classification): scikit-learn (For training the fake review detection model)

Natural Language Processing: sentence-transformers (Hugging Face models for generating text embeddings)

Vector Database: chromadb (For storing embeddings and executing fast semantic similarity searches)

📂 Project Architecture & MVP Approach

To ensure high performance and focus strictly on the AI/ML implementation, this Minimum Viable Product (MVP) operates on a static, curated dataset (products.csv) rather than utilizing live web-scraping. This architectural decision bypasses the aggressive anti-bot protections of major retail sites, allowing the semantic search and classification algorithms to run seamlessly without network bottlenecks.

Directory Structure:

Plaintext
prism-marketplace/
│
├── app.py                 # Main Streamlit application and UI layout
├── model.py               # Core ML logic (Search embeddings & Review classifier)
├── data_prep.py           # Script for cleaning and formatting the initial dataset
├── products.csv           # Static database of products, prices, and sample reviews
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
💻 Local Setup & Installation

Follow these steps to run P.R.I.S.M. on your local machine.

1. Clone the Repository

Bash
git clone https://github.com/[YOUR_USERNAME]/prism-marketplace.git
cd prism-marketplace
2. Create a Virtual Environment
It is highly recommended to use an isolated environment to prevent dependency conflicts.

Bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Dependencies

Bash
pip install -r requirements.txt
4. Launch the Application
Start the Streamlit server to view the web interface.

Bash
streamlit run app.py
The application will automatically open in your default web browser at http://localhost:8501.

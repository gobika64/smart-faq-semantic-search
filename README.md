# 🤖 Smart FAQ Semantic Search System

## 📌 Overview
This project is an AI-powered FAQ search system that retrieves the most relevant answer based on user queries using semantic similarity.

## 🚀 Features
- Semantic search using embeddings
- Real-world FAQ dataset
- Fast and accurate results
- Simple and scalable design

## 🧠 How It Works
1. FAQs are converted into vector embeddings
2. User query is converted into embedding
3. Cosine similarity is used to compare
4. Best matching answer is returned

## 🔗 Relation to Vector Databases
This system simulates how vector databases like Endee:
- Store embeddings
- Perform similarity search
- Retrieve relevant responses

## ▶️ How to Run

pip install -r requirements.txt  
python app.py  

## 💬 Example

Input:
How can I change my password?

Output:
Click on forgot password and follow steps.

## 📈 Future Improvements
- Integrate with real vector database (Endee)
- Add web interface (Streamlit)
- Support large-scale datasets

## 📷 Demonstration

![Output Screenshot](output.png)

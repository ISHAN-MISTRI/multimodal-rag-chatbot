# 📄 Multi-PDF RAG Chatbot

An intelligent chatbot that allows users to upload multiple PDF documents and ask questions based on their content using Retrieval-Augmented Generation (RAG).

## 🚀 Features

- Upload multiple PDFs
- Semantic search using FAISS
- Context-aware answers using OpenAI (GPT-4o-mini)
- Source attribution for answers
- FastAPI backend + Streamlit frontend

## 🧠 Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- FAISS
- OpenAI API

## 📂 Project Structure

backend/
  main.py
  rag/
frontend/
  app.py

## ⚙️ Setup

1. Clone repo
2. Install dependencies: pip install -r requirements.txt
3.  Add `.env` file: OPENAI_API_KEY=your_key_here

## ▶️ Run

Backend: 
uvicorn backend.main:app --reload

Frontend:
streamlit run frontend/app.py

## 💡 Usage

- Upload PDFs
- Ask questions
- Get answers with sources

## ⚠️ Note

- API key is required
- Do not upload `.env` file

## 👨‍💻 Author

Ishan Mistri

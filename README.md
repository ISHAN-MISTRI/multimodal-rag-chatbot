# 🧠 Multimodal RAG Chatbot with OCR

A FastAPI + Streamlit based Multimodal RAG (Retrieval-Augmented Generation) chatbot that supports:

- 📄 PDF Question Answering
- 🖼️ OCR-based Image Text Extraction
- 📑 Scanned PDF Processing
- 🔍 Semantic Search using FAISS
- 🤖 Context-aware AI Responses using OpenAI

---

# 🚀 Features

## ✅ Multi-PDF Upload
Users can upload multiple PDFs simultaneously.

## ✅ OCR Support
Extracts text from:
- PNG
- JPG
- JPEG
- Scanned PDFs

using Tesseract OCR.

## ✅ Intelligent Retrieval
- Semantic chunk retrieval
- Embedding-based search
- Source-aware filtering
- Dynamic query routing

## ✅ Context-Grounded Responses
The chatbot answers ONLY from uploaded document/image context to reduce hallucinations.

---

# 🏗️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM | OpenAI GPT-4o |
| Embeddings | OpenAI Embeddings |
| Vector DB | FAISS |
| OCR Engine | Tesseract OCR |
| Framework | LangChain |

---

# 📂 Project Structure

```bash
RAG-CHATBOT/
│
├── backend/
│   ├── main.py
│   └── rag/
│       ├── loader.py
│       ├── splitter.py
│       ├── embeddings.py
│       ├── vectorstore.py
│       ├── rag_chain.py
│       └── ocr.py
│
├── frontend/
│   └── app.py
│
├── temp/
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd RAG-CHATBOT
```

---

## 2️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Setup Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_api_key
```

---

# 🔧 OCR Setup

## Install Tesseract OCR

Download:
https://github.com/UB-Mannheim/tesseract/wiki

Install and update path inside:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# ▶️ Running the Application

## Start Backend

```bash
uvicorn backend.main:app --reload
```

---

## Start Frontend

```bash
streamlit run frontend/app.py
```

---

# 🧪 Example Queries

## PDF Queries
- Compare EBITDA across reports
- Summarize SUV market share trends

## OCR Image Queries
- What text is written in the uploaded image?
- Extract ticket price and date from image
- Which teams are present in the IPL ticket image?

---

# 🧠 OCR Improvements Implemented

- Image resizing
- Grayscale conversion
- Thresholding
- OCR confidence estimation
- Image-aware retrieval filtering

---

# 📌 Future Improvements

- Persistent vector database
- Chat memory
- Hybrid search
- Docker deployment
- Authentication system
- Advanced OCR models

---

# 👨‍💻 Author

Ishan Mistri

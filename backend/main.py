from fastapi import FastAPI, UploadFile, File
import os

from backend.rag.loader import load_all_pdfs
from backend.rag.splitter import split_docs
from backend.rag.embeddings import get_embeddings
from backend.rag.vectorstore import create_vectorstore
from backend.rag.rag_chain import create_rag_chain


app = FastAPI()

qa = None
processed = False


@app.post("/upload/")
async def upload(files: list[UploadFile] = File(...)):
    global qa, processed

    if processed:
        return {"message": "Already processed"}

    processed = True

    # create temp folder
    os.makedirs("temp", exist_ok=True)

    # save uploaded files
    for file in files:
        file_path = f"temp/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

    # build RAG pipeline
    docs = load_all_pdfs("temp")
    chunks = split_docs(docs)
    embeddings = get_embeddings()
    db = create_vectorstore(chunks, embeddings)
    qa = create_rag_chain(db)

    return {"message": "PDFs processed successfully"}


@app.get("/ask/")
def ask(query: str):
    if not qa:
        return {"error": "Upload PDFs first"}

    answer = qa(query)
    return {"answer": answer}

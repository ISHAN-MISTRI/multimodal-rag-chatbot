from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings):
    db = FAISS.from_documents(chunks, embeddings)

    print("Vector store created")

    return db

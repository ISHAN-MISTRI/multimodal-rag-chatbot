import streamlit as st
import requests

st.title("📄 Multi-PDF Chatbot")

uploaded_files = st.file_uploader(
    "Upload Files",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    files = [("files", (f.name, f.getvalue())) for f in uploaded_files]

    res = requests.post("http://localhost:8000/upload/", files=files)
    st.success("PDFs uploaded and processed!")

query = st.text_input("Ask your question")

if st.button("Ask"):
    with st.spinner("Thinking... "):
        res = requests.get(
            "http://localhost:8000/ask/",
            params={"query": query}
        )
        st.success("Answer:")
        st.write(res.json()["answer"])

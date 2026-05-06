from langchain_openai import ChatOpenAI


def create_rag_chain(db):

    retriever = db.as_retriever()

    llm = ChatOpenAI(model="gpt-4o")

    def ask(query):

        query_lower = query.lower()

        # enhance image-related queries
        if "image" in query_lower:
            query += " OCR extracted image text"

        # retrieve docs
        docs = retriever.invoke(query, k=10)

        # IMAGE FILTERING
        if "image" in query_lower:

            image_docs = []

            for doc in docs:
                if doc.metadata.get("type") == "image":
                    image_docs.append(doc)

            # use only image docs if found
            if image_docs:
                docs = image_docs

        # build context
        context = ""
        sources = []

        for doc in docs:
            context += doc.page_content + "\n\n"
            sources.append(doc.metadata.get("source", "unknown"))

        # prompt
        prompt = f"""
You are an intelligent document analysis assistant.

STRICT RULES:
- Use ONLY the provided context
- OCR text may contain noisy or imperfect extraction
- Infer structured information carefully
- Never say you cannot view images
- OCR extracted text from uploaded images is also part of the context
- If answer exists in context, answer confidently
- If information truly does not exist, say "Not found in uploaded documents"

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        unique_sources = list(set(sources))

        source_text = "\n".join([f"- {s}" for s in unique_sources])

        return (
            response.content
            + f"\n\n📄 Sources:\n{source_text}"
        )

    return ask

from langchain_openai import ChatOpenAI


def create_rag_chain(db):
    retriever = db.as_retriever()

    llm = ChatOpenAI(model="gpt-4o")

    def ask(query):
        docs = retriever.invoke(query, k=8)

        context = ""
        sources = []

        for doc in docs:
            context += doc.page_content + "\n\n"
            sources.append(doc.metadata.get("source", "unknown"))

        prompt = f"""
You are a financial analyst.

STRICT RULES:
- Use ONLY the context
- Try to interpret financial terms flexibly
- "price performance" may appear as stock movement, returns, growth, etc.
- "stock performance" may include margins, growth, revenue trends
- Do NOT say "not found" unless absolutely no relevant data exists
- Compare across reports if possible

Context:
{context}

Question:
{query}
"""

        response = llm.invoke(prompt)

        return response.content + f"\n\nSources: {set(sources)}"

    return ask

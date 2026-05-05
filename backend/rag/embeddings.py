from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def get_embeddings():
    return OpenAIEmbeddings()

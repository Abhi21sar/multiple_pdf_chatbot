from typing import List
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from src.core.config import settings
from src.core.logger import logger

class VectorStoreService:
    @staticmethod
    def create_vector_store(text_chunks: List[str]):
        """Creates a FAISS vector store from text chunks."""
        try:
            embeddings = OpenAIEmbeddings(
                openai_api_key=settings.OPENAI_API_KEY,
                model=settings.DEFAULT_EMBEDDING_MODEL
            )
            vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
            return vectorstore
        except Exception as e:
            logger.error(f"Error creating vector store: {e}")
            raise e

    @staticmethod
    def load_vector_store(path: str):
        """Loads a vector store from disk."""
        # Implementation for persistence can be added here
        pass

from typing import List
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.core.logger import logger
from src.core.config import settings

class PDFProcessor:
    @staticmethod
    def extract_text_from_pdfs(pdf_docs) -> str:
        """Extracts text from a list of PDF documents."""
        text = ""
        for pdf in pdf_docs:
            try:
                pdf_reader = PdfReader(pdf)
                for page in pdf_reader.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"
            except Exception as e:
                logger.error(f"Error extracting text from PDF: {e}")
        return text

    @staticmethod
    def get_text_chunks(text: str) -> List[str]:
        """Splits text into manageable chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_text(text)
        return chunks

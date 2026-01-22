import pytest
from unittest.mock import MagicMock
from src.services.pdf_processor import PDFProcessor

def test_extract_text_from_pdfs_empty():
    """Test text extraction from an empty list of PDFs."""
    text = PDFProcessor.extract_text_from_pdfs([])
    assert text == ""

def test_get_text_chunks():
    """Test text chunking logic."""
    text = "This is a test sentence that should be split into multiple chunks if it's long enough."
    # Set small chunk size for testing
    from src.core.config import settings
    original_chunk_size = settings.CHUNK_SIZE
    settings.CHUNK_SIZE = 20
    settings.CHUNK_OVERLAP = 0
    
    chunks = PDFProcessor.get_text_chunks(text)
    
    assert len(chunks) > 1
    # Restore settings
    settings.CHUNK_SIZE = original_chunk_size

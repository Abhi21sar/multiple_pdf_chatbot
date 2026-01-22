import streamlit as st
from dotenv import load_dotenv
from src.core.logger import logger
from src.core.config import settings
from src.services.pdf_processor import PDFProcessor
from src.services.vector_store import VectorStoreService
from src.services.llm_service import LLMService
from src.ui.components import render_header, render_sidebar, render_chat_message
from src.ui.styles import apply_custom_styles

def initialize_session_state():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "process_complete" not in st.session_state:
        st.session_state.process_complete = False

def handle_user_input(user_question):
    if st.session_state.conversation:
        with st.spinner("Thinking..."):
            response = st.session_state.conversation({'question': user_question})
            st.session_state.chat_history = response['chat_history']
            
            # Display chat history
            for i, message in enumerate(st.session_state.chat_history):
                is_user = (i % 2 == 0)
                render_chat_message(message.content, is_user=is_user)
    else:
        st.warning("Please upload and process your documents first!")

def main():
    load_dotenv()
    render_header()
    apply_custom_styles()
    initialize_session_state()

    pdf_docs, process_button, model_choice, temperature = render_sidebar()

    if process_button:
        if not pdf_docs:
            st.error("Please upload at least one PDF.")
        else:
            with st.spinner("Processing documents..."):
                try:
                    # 1. Extract Text
                    raw_text = PDFProcessor.extract_text_from_pdfs(pdf_docs)
                    
                    # 2. Get Chunks
                    text_chunks = PDFProcessor.get_text_chunks(raw_text)
                    
                    # 3. Create Vector Store
                    vectorstore = VectorStoreService.create_vector_store(text_chunks)
                    
                    # 4. Create Conversation Chain
                    st.session_state.conversation = LLMService.get_conversation_chain(vectorstore)
                    
                    st.session_state.process_complete = True
                    st.success("Documents processed successfully! You can now ask questions.")
                except Exception as e:
                    st.error(f"An error occurred during processing: {str(e)}")
                    logger.exception("Processing failed")

    # Main chat interface
    user_question = st.chat_input("Ask a question about your documents:")
    
    if user_question:
        handle_user_input(user_question)
    elif not st.session_state.chat_history and st.session_state.process_complete:
        st.info("Ask your first question above! 👆")

if __name__ == "__main__":
    main()

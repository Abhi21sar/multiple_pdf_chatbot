import streamlit as st
from src.ui.styles import bot_template, user_template

def render_chat_message(message, is_user=True):
    template = user_template if is_user else bot_template
    st.markdown(template.replace("{{MSG}}", message), unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.title("⚙️ Configuration")
        st.markdown("---")
        
        # Model Selection
        model_choice = st.selectbox(
            "Select LLM Model",
            ["gpt-3.5-turbo", "gpt-4-turbo-preview", "claude-3-opus-20240229"]
        )
        
        # Temperature Slider
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
        
        st.markdown("---")
        st.subheader("📚 Your Documents")
        pdf_docs = st.file_uploader(
            "Upload PDFs", 
            accept_multiple_files=True,
            type=["pdf"]
        )
        
        process_button = st.button("🚀 Process Documents")
        
        return pdf_docs, process_button, model_choice, temperature

def render_header():
    st.set_page_config(
        page_title="Pro PDF Chatbot",
        page_icon="📚",
        layout="wide"
    )
    st.title("📚 Pro PDF Chatbot")
    st.markdown("""
        Unlock the knowledge within your PDFs. Upload multiple documents and start a conversation.
    """)
    st.markdown("---")

# 📚 Pro PDF Chatbot

A professional, industrial-grade Retrieval-Augmented Generation (RAG) application that allows you to chat with multiple PDF documents simultaneously. Built with LangChain, OpenAI, and Streamlit.

## ✨ Features

- **Multi-PDF Support**: Upload and process multiple PDF files at once.
- **Advanced RAG**: Uses `RecursiveCharacterTextSplitter` for better context preservation and FAISS for efficient similarity search.
- **Modular Architecture**: Clean separation of concerns between UI, services, and core configuration.
- **Premium UI**: Modern, responsive interface with custom CSS and structured chat components.
- **Configurable**: Easily switch between models and tweak RAG parameters via `.env` or the UI sidebar.
- **Robust Error Handling**: Comprehensive logging and error reporting.

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10 or higher
- [Poetry](https://python-poetry.org/docs/#installation) (recommended) or pip

### 2. Installation

Clone the repository:
```bash
git clone https://github.com/your-repo/multiple_pdf_chatbot.git
cd multiple_pdf_chatbot
```

Install dependencies:
```bash
# Using Poetry
poetry install

# Using pip
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```
Add your OpenAI API key to the `.env` file:
```env
OPENAI_API_KEY=sk-your-key-here
```

### 4. Running the App
```bash
streamlit run app.py
```

## 🏗️ Project Structure

```text
multiple_pdf_chatbot/
├── src/
│   ├── app.py             # Main entry point for Streamlit
│   ├── core/              # Config, logging, constants
│   ├── services/          # Core logic (PDF, Vector Store, LLM)
│   └── ui/                # UI components and styles
├── tests/                 # Unit and integration tests
├── .env                   # Environment variables (not in git)
├── pyproject.toml         # Poetry dependencies
└── app.py                 # Root entry point wrapper
```

## 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **Orchestration**: [LangChain](https://python.langchain.com/)
- **Embeddings**: [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)
- **LLM**: [GPT-3.5/4](https://openai.com/)

## 📄 License
MIT License

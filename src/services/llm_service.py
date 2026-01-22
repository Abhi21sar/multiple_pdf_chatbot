from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationalRetrievalChain
from src.core.config import settings
from src.core.logger import logger

class LLMService:
    @staticmethod
    def get_conversation_chain(vectorstore):
        """Creates a conversational retrieval chain."""
        try:
            llm = ChatOpenAI(
                openai_api_key=settings.OPENAI_API_KEY,
                model_name=settings.DEFAULT_MODEL,
                temperature=0.7
            )
            
            memory = ConversationBufferMemory(
                memory_key='chat_history',
                return_messages=True,
                output_key='answer'
            )
            
            conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
                memory=memory,
                return_source_documents=True
            )
            return conversation_chain
        except Exception as e:
            logger.error(f"Error creating conversation chain: {e}")
            raise e

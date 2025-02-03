import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Load environment variables
load_dotenv()

# Retrieve API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("⚠️ OpenAI API Key not found. Please set it in a .env file.")

# Set up Streamlit UI
st.title("💬 BongAI")
st.write("A chatbot powered by LangChain and OpenAI.")

# Initialize Chat Model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

# Create VectorStore (Optional)
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.from_texts(["Hello, how can I help you today?"], embeddings)
retriever = vectorstore.as_retriever()

# Setup Conversational Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm, retriever=retriever,
    return_source_documents=True  # Optional
)

# Chat Input and History Management
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", "", key="user_input")

if user_input:
    # Convert chat history to expected format (list of tuples)
    chat_history = [(msg["role"], msg["content"]) for msg in st.session_state.chat_history]

    try:
        # Call LangChain QA Chain
        response = qa_chain.invoke({"question": user_input, "chat_history": chat_history})
        response_text = response['answer']
    except Exception as e:
        st.error(f"An error occurred: {e}")
        response_text = "Sorry, I couldn't process your request."

    # Append new conversation turn to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response_text})

# Display Chat History
for message in st.session_state.chat_history:
    st.write(f"**{message['role'].capitalize()}:** {message['content']}")
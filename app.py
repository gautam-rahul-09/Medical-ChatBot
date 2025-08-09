import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage

# Load environment variables
load_dotenv()
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Initialize Azure OpenAI model
llm = AzureChatOpenAI(
    deployment_name=AZURE_DEPLOYMENT_NAME,
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2023-05-15"
)

# Streamlit Page Configuration
st.set_page_config(page_title="🩺 Medical Chatbot", layout="centered")

# Custom CSS for background and chat bubbles
st.markdown("""
    <style>
    body, .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .user-message {
        background-color: #00b36b;
        color: white;
        padding: 10px 15px;
        border-radius: 20px;
        margin: 10px 0;
        display: inline-block;
        text-align: right;
        float: right;
        clear: both;
    }
    .bot-message {
        background-color: #3399ff;
        color: white;
        padding: 10px 15px;
        border-radius: 20px;
        margin: 10px 0;
        display: inline-block;
        text-align: left;
        float: left;
        clear: both;
    }
    .chat-container {
        padding: 20px;
        max-height: 500px;
        overflow-y: auto;
        border-radius: 10px;
    }
    .message-input textarea {
        background-color: #1a1a1a;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Chat Header
st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" width="60">
        <div style="margin-left: 10px;">
            <h2 style="margin: 0; color: #00d4ff;">Medical Chatbot</h2>
            <p style="margin: 0; color: #aaa;">Ask me anything!</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize session state for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div class='user-message'>{chat['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{chat['content']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Input form
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("Type your message...", label_visibility="collapsed")
    submitted = st.form_submit_button("Send")

# Process input
if submitted and user_query:
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    with st.spinner("Thinking..."):
        try:
            response = llm.invoke([HumanMessage(content=user_query)])
            st.session_state.chat_history.append({"role": "bot", "content": response.content})
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    st.rerun()


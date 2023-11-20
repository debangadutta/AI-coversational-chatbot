import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#streamlit UI
st.set_page_config(page_title="Conversational Chatbot")
st.header("Hey! What's up?")
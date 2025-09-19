
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from rag_chain import get_chain
from langchain_core.output_parsers import StrOutputParser
import os  #for macOS TTS
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 RAG Chatbot")

# --- Initialize Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chain = get_chain(st.session_state.chat_history)

# --- Slidebar Controls ---
on = st.sidebar.toggle("Text-To-Speech")
if on:
    st.sidebar.write("TTS Enabled")

if st.sidebar.button('CLEAR 🗑'):
    st.session_state.chat_history.clear()

if st.button("Add Docs"):
    st.switch_page("pages/docloaderui.py") 

# --- Display Previous Messages ---
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

parser = StrOutputParser() # Ensure outputs are strings

if st.sidebar.button('rec'):
    user_input = st.chat_input("Type your message here...")
    with st.spinner("Speak something..."):
        with sr.Microphone() as source:
            audio = recognizer.listen(source,phrase_time_limit=5)

        try:
            text = recognizer.recognize_google(audio)
            user_input=text
        except sr.UnknownValueError:
            st.error("❌ Could not understand audio")
else:
    user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Get AI response
    output = st.session_state.chain.invoke(user_input)

    st.session_state.chat_history.append(AIMessage(content=output))
    with st.chat_message("assistant"):
        st.write(output)
        if on:
            os.system(f'say "{output}"')

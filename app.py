import streamlit as st
import asyncio
from langchain_core.messages import HumanMessage, AIMessage
from rag_chain import get_chain
st.title("🤖 RAG Chatbot")

# try:
#     asyncio.get_running_loop()
# except RuntimeError:
#     asyncio.set_event_loop(asyncio.new_event_loop())

chat_history = []
chain = get_chain(chat_history)

print("🤖 Chatbot is ready! Type 'exit' to quit.\n")

user_input=st.text_input('Enter your promt')

if st.button('Answer'):
    output = chain.invoke(user_input)
    st.write(output)
    chat_history.append(AIMessage(content=output))






# ##app.py
# import asyncio
# import streamlit as st
# from langchain_core.messages import HumanMessage, AIMessage
# from rag_chain import get_chain

# # --- Fix: ensure an event loop exists (Streamlit runs in its own thread) ---
# try:
#     asyncio.get_running_loop()
# except RuntimeError:
#     asyncio.set_event_loop(asyncio.new_event_loop())

# # --- Streamlit UI config ---
# st.set_page_config(page_title="🤖 RAG Chatbot", page_icon="🤖")
# st.title("🤖 RAG Chatbot")
# st.caption("Ask questions about your ingested PDFs. Answers come strictly from context.")

# # --- Chat history ---
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []  # list[HumanMessage | AIMessage]

# def build_chain():
#     """Builds a chain with current chat history."""
#     return get_chain(st.session_state.chat_history)

# # --- Display previous messages ---
# for msg in st.session_state.chat_history:
#     role = "assistant" if isinstance(msg, AIMessage) else "user"
#     with st.chat_message(role):
#         st.write(msg.content)

# # --- Input box at bottom ---
# user_input = st.chat_input("Type your question here...")

# if user_input:
#     # Save user message
#     st.session_state.chat_history.append(HumanMessage(content=user_input))
#     with st.chat_message("user"):
#         st.write(user_input)

#     # Run chain
#     try:
#         chain = build_chain()
#         # Use async-safe call
#         output = asyncio.run(chain.ainvoke(user_input))
#     except Exception as e:
#         output = f"❌ Error: {e}"

#     # Save AI response
#     st.session_state.chat_history.append(AIMessage(content=output))
#     with st.chat_message("assistant"):
#         st.write(output)

# # --- Sidebar controls ---
# st.sidebar.header("⚙️ Options")
# if st.sidebar.button("🧹 Clear Chat"):
#     st.session_state.chat_history = []
#     st.rerun()

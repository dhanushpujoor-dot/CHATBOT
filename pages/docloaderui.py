import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader,TextLoader,CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import streamlit as st
import shutil

load_dotenv()
apikey=os.getenv("GOOGLE_API_KEY")

st.title("📁 Upload a File")
uploaded_file = st.file_uploader("Choose a file")

if st.button("⬅️ Back to ChatBot"):
    st.switch_page("app.py")

def ingest_data(path):

    if uploaded_file.type == 'application/pdf':
        loader=PyPDFLoader(file_path=path)
    elif uploaded_file.type == 'text/plain':
        loader=TextLoader(file_path=path,encoding='utf-8')
    elif uploaded_file.type == 'text/csv':
        loader=CSVLoader(file_path=path)
    else:
        st.error("Unsupported file type")
        return
        
    docs=loader.load()

    if st.button('Split n Ingest'):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(docs)

        vector_store = Chroma(
            embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L12-v2"),
            collection_name="sample",
            persist_directory="./chatbot_db"
        )
        vector_store.add_documents(chunks)
        st.write(f"✅ Ingested {len(chunks)} chunks into Chroma DB")

    if st.button('Clear DB'):
        if os.path.exists("chatbot_db"):
            shutil.rmtree("chatbot_db")
            st.write("Chroma DB Cleared")
        else:
            st.write("No DB found to clear.")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.write("File type:", uploaded_file.type)
    ingest_data(path=uploaded_file.name)


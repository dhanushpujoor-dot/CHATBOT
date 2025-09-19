from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import shutil
import os

load_dotenv()

def ingest_data(path):       
    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )
    chunks = splitter.split_documents(docs)
    
    #embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001",api_key=api_key)
    # embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-base-en")
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L12-v2")

    user = input('clear vector db(y/n): ')
    if user.lower() == 'y':
        if os.path.exists("chatbot_db"):
            shutil.rmtree("chatbot_db")
            print("Chroma DB Cleared")
        else:
            print("No DB found to clear.")
        return

    vector_store = Chroma(
        embedding_function=embedding,
        collection_name="sample",
        persist_directory="./chatbot_db"
    )

    vector_store.add_documents(chunks)
    print(f"✅ Ingested {len(chunks)} chunks into Chroma DB")

if __name__ == "__main__":
    ingest_data("dl-curriculum.pdf")

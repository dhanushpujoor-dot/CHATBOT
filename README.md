# 🤖 Chatbot Project
A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, Streamlit, Python and Hugging Face.

---

## 📂 Project Structure

```
chatbot/
│── app.py             # Streamlit UI
│── main.py            # Main script
│── rag_chain.py       # RAG pipeline
│── data_ingestion.py  # Data ingestion scripts
│── docloaderui.py     # Document loader UI
│── tts.py             # Text-to-speech
│── chatbot_db/        # Vector database
│── Panchatantra.pdf   # Example document
│── README.md          # Project instructions
```

---

## 🔑 Set up environment variables
Create a `.env` file in the root with your API keys:
```
OPENAI_API_KEY=your_api_key_here
```
(or use `GOOGLE_API_KEY=...` if you’re using Google GenAI)

---

## ▶️ Running the App

### 🔹 UI Mode (Streamlit)
Run these scripts for the chatbot with UI:
```bash
python docloaderui.py
streamlit run app.py
```

### 🔹 Normal Python Mode
Run these scripts for the terminal-based chatbot:
```bash
python data_ingestion.py
python main.py
```

---

✅ **Note:**  
- You do **not** need to run `rag_chain.py` directly.  
- It’s automatically imported by `main.py` and `app.py`.  

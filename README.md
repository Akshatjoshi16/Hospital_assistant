# 🏥 Hospital Operations Knowledge Bot

A **RAG-based (Retrieval-Augmented Generation) chatbot** designed to answer queries related to hospital operations such as patient admission, ICU protocols, billing, and workflows.

---

## 🚀 Features

* 📄 Answers based on real hospital documents (PDFs)
* 🤖 Uses LLM for intelligent and structured responses
* 🔍 Semantic search using vector database (FAISS)
* 💬 Chat-based UI with history (Streamlit)
* 🛡 Safety layer using Detoxify & Presidio
* ⚡ Fast inference using Groq (Llama model)

---

## 🧠 Architecture (RAG)

User Query → Embedding → FAISS → Retrieve Relevant Docs → LLM → Answer

---

## 🛠 Tech Stack

* **LLM**: Groq (Llama 3.3-70B Versatile)
* **Framework**: LangChain
* **Embeddings**: HuggingFace (sentence-transformers)
* **Vector DB**: FAISS
* **Frontend**: Streamlit
* **Document Loader**: PyPDFLoader, DirectoryLoader
* **Text Splitting**: RecursiveCharacterTextSplitter
* **Guardrails**: Detoxify, Presidio
* **Environment Management**: python-dotenv

---

## 📁 Project Structure

hospital_assistant/

├── frontend.py          # Streamlit UI
├── rag_qa.py           # RAG pipeline logic
├── model.py            # LLM configuration (Groq)
├── guardrails.py       # Safety checks

├── ingestion/
│   ├── loaddoc.py      # Load PDF documents
│   ├── chunking.py     # Split documents
│   ├── embed.py        # Embedding model
│   ├── vecdb.py        # FAISS database
│   └── hospital_docs/  # Hospital PDFs

├── requirements.txt
├── .env
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/Akshatjoshi16/Hospital_assistant.git
cd hospital_assistant

---

### 2. Create virtual environment

python -m venv .venv

Activate (Windows):

.venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Add environment variables

Create a `.env` file:

GROQ_API_KEY=your_api_key_here

---

### 5. Run the application

streamlit run frontend.py

---

## 🧪 Example Queries

* What is patient admission process?
* Explain ICU protocol
* How hospital billing works?
* What are hospital departments?

---

## 🎯 Key Concepts Used

* RAG (Retrieval-Augmented Generation)
* Embeddings for semantic understanding
* Vector similarity search (FAISS)
* Prompt engineering

---

## ⚠️ Limitations

* Depends on quality of input PDFs
* Cannot answer outside provided documents
* Retrieval may sometimes miss context

---

## 🔮 Future Improvements

* Doctor recommendation system
* Appointment booking system
* Disease prediction module
* Voice-based interaction

---

## 👨‍💻 Author

Akshat Joshi

---

## ⭐ One-line Summary

A RAG-based chatbot that retrieves hospital knowledge from documents and generates accurate responses using Groq LLM.

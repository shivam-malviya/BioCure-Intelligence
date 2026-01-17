# 🧬 BioCure Intelligence  
### AI-Powered PubMed Literature Assistant (RAG-based)

BioCure Intelligence is a **Retrieval-Augmented Generation (RAG)** application that leverages **PubMed biomedical literature** and **Google Gemini** to provide research-based insights about diseases.

⚠️ This application is intended **only for educational and research purposes** and **must not be used as medical advice**.

---

## 🚀 Features

- 🔍 Disease-based search using **PubMed**
- 📄 Automatic web content loading from PubMed URLs
- 🧠 Semantic search using **HuggingFace embeddings**
- 📚 Vector storage with **ChromaDB**
- 🤖 AI-powered answers using **Google Gemini**
- 🌐 Interactive **Streamlit** frontend
- 🌍 Automatic translation of responses into **Hindi**

---

## 🧠 Tech Stack

- **Python**
- **LangChain**
- **Google Gemini (Generative AI)**
- **HuggingFace Sentence Transformers**
- **Chroma Vector Database**
- **Unstructured**
- **Streamlit**

---

## 🏗️ Architecture (RAG Pipeline)

User Query
↓
PubMed URL Fetching
↓
Unstructured URL Loader
↓
Text Chunking
↓
Embeddings (HuggingFace)
↓
Vector Store (Chroma)
↓
Retriever
↓
Gemini LLM
↓
Answer + Sources


## Create virtual environment (recommended)

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

## Install dependencies

pip install -r requirements.txt


## ▶️ Run the Application

streamlit run app.py

    Then open: http://localhost:8501


## 🧪 Example Usage

Enter a disease name (e.g. Alzheimer disease)

The system:

    Searches PubMed

    Retrieves relevant biomedical literature

    Generates an AI-powered summary

    Translates the output into Hindi



## ⚠️ Medical Disclaimer

This application does NOT provide medical advice, diagnosis, or treatment.
The information generated is based on publicly available research literature and should not be used as a substitute for professional healthcare consultation.


## 📌 Limitations

PubMed pages may change structure

Gemini responses depend on retrieved context

Not optimized for clinical decision-making

Requires internet access


## 🛣️ Future Improvements

✅ PubMed API integration (instead of HTML scraping)

✅ Source citation display

✅ Disease confidence scoring

✅ Multi-language support

✅ Deployment on Streamlit Clou

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.


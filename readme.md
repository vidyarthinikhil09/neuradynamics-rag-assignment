# 🧠 Neuradynamics (Pragya) Policy RAG Agent

> **AI Engineering Intern Assignment Submission**  
> **Author:** Nikhil Kumar Vidyarthi  
> **Date:** February 2026  

---

## 📖 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system designed to serve as an intelligent FAQ assistant for **Pragya (Neuradynamics)**. The system enables users to ask questions related to the company's **Terms of Service** and **Privacy Policy**, returning accurate, grounded, and context-supported answers.

Unlike traditional chatbots, this agent is designed to be **conservative, factual, and safe**. It strictly refuses to answer questions outside its knowledge base, preventing hallucinations and ensuring reliability.

### 🎯 Problem Statement
Customers and internal support teams often need to manually search policy documents to find relevant clauses. This process is time-consuming and inefficient. This RAG system automates policy retrieval and explanation, improving accessibility and response accuracy.

---

## 🚀 Key Features

### 🔍 Semantic Search
Uses **ChromaDB** combined with **Google Gemini Embeddings** to retrieve the most relevant policy sections based on user queries.

### ⚡ Gemini 1.5 Flash Powered Reasoning
Leverages Google's **Gemini 1.5 Flash** model to generate fast, cost-efficient, and high-quality responses grounded in retrieved content.

### 🧪 Automated Evaluation Framework
Includes a testing suite (`evaluate.py`) that benchmarks system performance across:

- Answerable Queries
- Ambiguous Queries
- Unanswerable Queries

### 🛡️ Hallucination Prevention
The agent strictly follows prompt guardrails and refuses to fabricate answers when required information is unavailable.

---

## 🏗️ System Architecture

```
User Query
    ↓
Query Embedding (Gemini Embeddings)
    ↓
Vector Search (ChromaDB)
    ↓
Retrieve Relevant Policy Chunks
    ↓
Gemini 1.5 Flash LLM
    ↓
Grounded Answer + Source Context
```

---

## 📂 Project Structure

```
neuradynamics-rag/
├── data/
│   └── policy.txt            # Source document (Terms & Privacy Policy)
├── chroma_db/                # Local vector database (generated after ingestion)
├── ingest.py                 # Script for data loading, chunking, and indexing
├── rag_agent.py              # Chat interface and inference pipeline
├── evaluate.py               # Automated testing and evaluation framework
├── requirements.txt          # Python dependencies
├── .env                      # API key configuration (excluded from version control)
└── README.md                 # Project documentation
```

---

## 🛠️ Installation & Setup

### ✅ Prerequisites

- Python **3.10 or higher**
- Google Cloud API Key (Gemini access)

---

### 📥 Clone Repository

```bash
git clone https://github.com/vidyarthinikhil09/neuradynamics-rag-assignment.git
cd neuradynamics-rag-assignment
```

---

### 🧪 Create Virtual Environment

```bash
python -m venv venv
```

#### Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

---

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install langchain-google-genai langchain-chroma langchain-community python-dotenv pandas tabulate
```

---

### 🔑 Configure API Key

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

---

## 🏃 Usage Guide

The system operates in two main stages:

---

### 🧠 Step 1: Data Ingestion (Build Knowledge Base)

```bash
python ingest.py
```

✔ Loads policy document  
✔ Splits into semantic chunks  
✔ Generates embeddings  
✔ Stores vectors in ChromaDB  

Expected Output:

```
Ingestion complete! Database rebuilt with Gemini embeddings.
```

---

### 💬 Step 2: Run RAG Agent

```bash
python rag_agent.py
```

Users can type policy-related questions interactively.

To exit:
```
exit
```
or
```
quit
```

---

### 📊 Step 3: Run Automated Evaluation

```bash
python evaluate.py
```

Results are generated in:

```
evaluation_report.md
```

---

## 🧠 Architecture & Design Decisions

---

### 📑 Chunking Strategy

- **Chunk Size:** 1000 characters  
- **Overlap:** 200 characters  

#### Reasoning
Legal documents contain dense contextual information. Overlapping chunks preserve continuity and improve retrieval accuracy.

---

### ✍️ Prompt Engineering Evolution

#### Iteration 1 (Initial Prompt)
```
You are a helpful assistant. Answer the user question based on the context.
```

❌ Result: Occasional hallucinations and speculative answers.

---

#### Iteration 2 (Final Prompt)
```
You are an intelligent assistant for Pragya. Answer strictly using provided context.

RULES:
1. Use ONLY the provided context.
2. If answer is missing, respond:
"I cannot answer this question using the provided policy documents."
```

✅ Result: Reliable grounded responses and safe refusal handling.

---

### ⚙️ Tech Stack Justification

| Technology | Purpose | Reason for Selection |
|------------|------------|----------------------|
| LangChain | RAG orchestration | Simplifies pipeline integration |
| ChromaDB | Vector storage | Lightweight and open-source |
| Gemini Embeddings | Semantic understanding | High-quality contextual vectorization |
| Gemini 1.5 Flash | LLM reasoning | Fast inference and large context window |

---

## 📊 Evaluation Results

| Category | Description | Performance |
|------------|----------------|----------------|
| Answerable | Clearly present in document | ✅ 100% Retrieval Accuracy |
| Edge Cases | Requires combining multiple clauses | ✅ Consistent Logical Responses |
| Unanswerable | Information not present in policy | ✅ Correct Refusal Behaviour |

---

### 🧪 Evaluation Methodology

- Structured query test dataset
- Manual ground truth comparison
- Behavioral validation for refusal scenarios

---

## ⚡ Performance Observations

- Fast query latency due to Gemini Flash model
- Efficient local vector retrieval using ChromaDB
- Stable performance across multi-clause queries

---

## 🛡️ Safety & Error Handling

- Explicit hallucination prevention via prompt constraints
- Graceful handling of missing context
- Secure API key storage using `.env`

---

## 🔮 Future Improvements

### 🔎 Hybrid Search
Combine semantic search with BM25 keyword search for improved retrieval recall.

### 🎯 Reranking Layer
Introduce cross-encoder or LLM reranking to improve precision.

### 📌 Source Highlighting
Return exact clause or line references.

### 🧠 Query Rewriting
Improve ambiguous query interpretation.

### 📊 Monitoring & Logging
Track query accuracy and model performance.

### 🖥️ UI Integration
Develop Streamlit or web interface for improved user experience.

---

## 💻 Tested Environment

- Python 3.10+
- Windows 11

---

## 📬 Contact

**Developed By:** Nikhil Kumar Vidyarthi  
**Email:** vidyarthinikhil5@gmail.com   
**GitHub:** [\[Your GitHub Profile\]](https://github.com/vidyarthinikhil09)

---

## ⭐ Acknowledgements

- LangChain Framework
- Google Gemini API
- ChromaDB Vector Store

---

## 📄 License

This project is developed for educational and evaluation purposes.

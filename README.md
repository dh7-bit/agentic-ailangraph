# 🤖 Agentic RAG System with Docker Deployment & Vectorless RAG Exploration

An advanced Retrieval-Augmented Generation (RAG) project exploring two distinct retrieval paradigms:

1. **Agentic RAG** – Tool-based document upload and retrieval agents with Dockerized deployment.
2. **Vectorless RAG** – Structured page-index traversal and LLM-based routing without embedding vectors.

This project demonstrates how retrieval architecture choices impact interpretability, scalability, deployment, and developer control in AI-powered document intelligence systems.

---

# 🚀 Features

## 🧠 Agentic RAG System

### 📤 Tool-Based Document Upload Agent

Upload documents dynamically through an agent-controlled workflow.

### 🔍 Intelligent Retrieval Agent

Dedicated retrieval agent responsible for document search and context extraction.

### 📚 Multi-Document Knowledge Base

Supports querying across multiple uploaded documents.

### ⚡ Retrieval-Augmented Generation

Combines document retrieval with LLM-powered response generation.

### 🐳 Dockerized Deployment

Containerized architecture enables portable and reproducible deployment.

---

## 🧭 Vectorless RAG System

### 📖 Page-Index Structured Retrieval

Navigates documents using hierarchical page and section indexes.

### 🧠 LLM-Based Routing

Language model selects relevant document sections instead of relying on embedding similarity.

### 🏗️ Hierarchical Document Navigation

Preserves document structure for improved interpretability.

### 🔍 Embedding-Free Retrieval

No vector database or embedding generation required.

### 📋 Transparent Retrieval Path

Developers can inspect exactly which document sections were selected.

---

# 🏗️ System Architecture

## Agentic RAG Workflow

```text
User Upload
      │
      ▼
Upload Tool Agent
      │
      ▼
Document Processing
      │
      ▼
Vector Store
      │
      ▼
Query Agent
      │
      ▼
Document Retrieval
      │
      ▼
LLM Generation
      │
      ▼
Response
```

---

## Vectorless RAG Workflow

```text
User Query
      │
      ▼
LLM Router
      │
      ▼
Page Index Traversal
      │
      ▼
Hierarchical Section Selection
      │
      ▼
Relevant Context
      │
      ▼
LLM Generation
      │
      ▼
Response
```

---

# 🔬 Research Objective

Traditional RAG systems rely heavily on dense vector embeddings for retrieval.

This project explores:

* How agentic workflows improve document handling.
* How Docker simplifies deployment and reproducibility.
* Whether structured document navigation can replace vector embeddings.
* Trade-offs between retrieval quality, interpretability, and system complexity.

---

# 📊 Comparison: Agentic RAG vs Vectorless RAG

| Feature                      | Agentic RAG | Vectorless RAG |
| ---------------------------- | ----------- | -------------- |
| Embeddings Required          | ✅ Yes       | ❌ No           |
| Vector Database              | ✅ Yes       | ❌ No           |
| Retrieval Transparency       | Moderate    | High           |
| Document Structure Awareness | Moderate    | High           |
| Semantic Similarity Search   | High        | Moderate       |
| Interpretability             | Moderate    | High           |
| Deployment Complexity        | Medium      | Low            |
| Hierarchical Navigation      | Limited     | Strong         |

---

# 🛠️ Tech Stack

## AI & Agents

* LangChain
* LangGraph
* LLM APIs (Groq / OpenAI)

## Vector-Based Retrieval

* ChromaDB
* FAISS

## Backend

* Python
* Flask / FastAPI

## Deployment

* Docker
* Docker Compose

## Vectorless Retrieval

* Page-Index Structured Knowledge Store
* LLM Routing Engine

---

# 📂 Project Workflow

## Agentic RAG

```text
Upload Document
      ↓
Upload Agent
      ↓
Processing & Indexing
      ↓
Vector Storage
      ↓
User Query
      ↓
Retrieval Agent
      ↓
LLM Response
```

---

## Vectorless RAG

```text
User Query
      ↓
LLM Router
      ↓
Page Selection
      ↓
Section Traversal
      ↓
Context Extraction
      ↓
LLM Response
```

---

# 🎯 Key Design Decisions

## ❌ Single Monolithic RAG Agent

Issue:

* Upload and retrieval logic tightly coupled
* Difficult to debug and extend

Decision:

* Split into dedicated Upload Agent and Retrieval Agent.

---

## ❌ Embedding-Only Retrieval for Structured Documents

Issue:

* Lost document hierarchy
* Reduced navigation interpretability

Decision:

* Developed page-index traversal architecture.

---

## ❌ Local Non-Containerized Deployment

Issue:

* Environment inconsistencies
* Difficult onboarding and sharing

Decision:

* Dockerized the entire application stack.

---

## ✅ Final Architecture

### Agentic RAG

* Upload Agent
* Retrieval Agent
* Vector Database
* LLM Response Generation
* Docker Deployment

### Vectorless RAG

* LLM Router
* Page-Index Traversal
* Structured Context Retrieval
* Embedding-Free Navigation

---

# 🐳 Docker Deployment

Build the image:

```bash
docker build -t agentic-rag .
```

Run the container:

```bash
docker run -p 8000:8000 agentic-rag
```

Using Docker Compose:

```bash
docker-compose up --build
```

Benefits:

* Portable deployment
* Consistent environments
* Easy reproducibility
* Simplified setup

---

# 📈 Key Outcomes

### Agentic RAG

✅ Dynamic document uploads

✅ Tool-based retrieval architecture

✅ Multi-document support

✅ Portable Docker deployment

---

### Vectorless RAG

✅ Embedding-free retrieval

✅ Hierarchical document navigation

✅ Interpretable retrieval paths

✅ Better control over structured knowledge sources

---

# 🔍 Additional Exploration

* Docker Compose orchestration
* Hybrid retrieval architectures
* Sparse keyword search integration
* LLM routing optimization
* Retrieval latency benchmarking
* Structured knowledge navigation strategies

---

# 📊 Project Impact

This project demonstrates that Retrieval-Augmented Generation extends beyond traditional embedding-based search.

By building both an Agentic RAG system and a Vectorless RAG alternative, the project highlights how retrieval architecture directly influences:

* Interpretability
* Scalability
* Developer control
* Deployment complexity
* Production readiness

The work provides practical insight into designing next-generation AI document systems that balance semantic understanding with transparent and controllable retrieval mechanisms.

---

# 🔗 GitHub Repository

Repository:

https://github.com/dh7-bit/agentic-ailangraph

---

# 👨‍💻 Author

Saksham Gupta

Agentic AI | LangGraph | LangChain | RAG Systems | Docker | NLP | AI Automation

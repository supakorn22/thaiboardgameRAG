# Boardgame RAG

A Retrieval-Augmented Generation (RAG) system for Thai language documents. This project includes a backend for document indexing and querying, and a demo for interacting with the system.

## 📁 Project Structure

```
.
├── notebook/          # Jupyter notebooks for testing and experimentation
├── mcp-rag-demo/      # MCP RAG demo interface
├── app/               # Main backend of the OpenThai RAG system
├── doc/               # Folder containing `.txt` files for embedding
└── docker-compose.yml
```

## 🚀 Getting Started

### 1. Start the System

```bash
docker-compose up -d
```

This will launch the services. The default query API runs on port `5001`.

### 2. Index Documents

To add embeddings to the Mulvis DB, run:

```bash
python app/index_docs.py
```

This script reads `.txt` files from the `/doc` directory and inserts their embeddings into the `document_embeddings` collection using `requests`.

> **Note:** You can change the target port in `app/index_docs.py` if needed.

---

## 📖 Querying the RAG

You can query documents via the following endpoints:

```
POST http://localhost:5001/completions
```

### Example Request Body

```json
{
  "prompt": "มีบอร์ดเกมอะไรที่ดัดแปลงมาจากการ์ตูนญี่ปุ่นเกี่ยวกับการสำรวจดันเจียนบ้าง?",
  "top_n": 10
}
```

---

## 🌐 Visual UI

You can also explore documents using the Mulvis ATT UI:

```
http://localhost:3000/
```

---

## 🛠 Requirements

- Python 3.8+
- Docker & Docker Compose
- `requests` (for document indexing)

---

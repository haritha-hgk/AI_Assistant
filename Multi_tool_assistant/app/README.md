# Local RAG Agent using LangGraph

A local AI assistant built with:

- LangGraph
- LangChain
- Ollama
- ChromaDB
- FastAPI
- RAG
- Streaming Responses
- Conversation Memory

## Features

- PDF Question Answering (RAG)
- Web Search Tool
- Calculator Tool
- LangGraph Agent
- Conversation Memory
- Streaming Responses
- FastAPI Backend
- HTML Chat Interface

## Tech Stack

- Python
- FastAPI
- LangGraph
- LangChain
- Ollama
- ChromaDB

## Installation

```bash
pip install -r requirements.txt
```

Download models:

```bash
ollama pull qwen2.5:7b
ollama pull nomic-embed-text
```

Create embeddings:

```bash
python app/ingest.py
```

Run server:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000
```
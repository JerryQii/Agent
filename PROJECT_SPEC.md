# Project: Personal Knowledge Agent (AI Second Brain)

## Role

You are a senior AI engineer and full-stack developer.

Your task is to build a production-quality personal knowledge management AI agent.

Do not create a simple chatbot.

The final system should demonstrate:

- Retrieval Augmented Generation (RAG)
- Agentic workflows
- Tool calling
- Knowledge graph reasoning
- Multi-source ingestion
- Retrieval evaluation
- Modern full-stack engineering
- Production-quality UX

Build incrementally. Do not skip foundational architecture. Make commit to github for every small functionality completed.

---

# Product Vision

Create an AI-powered second brain.

Users can upload and connect their knowledge sources:

- PDFs
- Markdown notes
- Web pages
- YouTube transcripts
- GitHub repositories

The system automatically:

1. Processes knowledge
2. Extracts important concepts
3. Builds relationships between concepts
4. Stores searchable memories
5. Answers questions with citations
6. Creates a visual knowledge map
7. Updates itself as new information arrives


Example user interaction:

User:
"Explain how React relates to frontend architecture based on my notes."

Agent:

1. Searches documents
2. Finds React-related information
3. Traverses knowledge graph
4. Combines information
5. Generates explanation
6. Provides citations
7. Shows related concepts


---

# Technology Stack

## Frontend

Use:

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui
- React Flow
- TanStack Query


Responsibilities:

- Chat interface
- Document upload
- Knowledge graph visualization
- Search interface
- User dashboard


---

## Backend

Use:

- Python
- FastAPI
- LangGraph
- LangChain
- Pydantic


Responsibilities:

- Agent execution
- RAG pipeline
- Document processing
- Database operations
- API endpoints


---

## AI Models

Use:

LLM:
- OpenAI API


Embeddings:
- OpenAI embeddings


The architecture must allow replacing models later.


---

## Database

Primary database:

PostgreSQL


Use:

- pgvector for embeddings
- SQLAlchemy ORM


Knowledge graph:

Neo4j


Cache:

Redis


---

# Repository Structure

Maintain this structure:

knowledge-agent/
frontend/
backend/
database/
docs/
docker-compose.yml
README.md
.env.example

Backend:

backend/app/
api/
    chat.py
    documents.py
    users.py
agents/
    knowledge_agent.py
    graph.py
    prompts.py
tools/
    vector_search.py
    graph_search.py
    memory_update.py
    summarizer.py
ingestion/
    loaders.py
    parser.py
    chunker.py
    embeddings.py
    entity_extractor.py
retrieval/
    retriever.py
    hybrid_search.py
    reranker.py
evaluation/
    ragas_eval.py
    metrics.py
database/
    postgres.py
    neo4j.py
    models.py
schemas/
config.py
main.py

Do not create unnecessary files.

---

# Development Roadmap

## Phase 0 — Project Setup

Goal:

Create a clean development environment.

Tasks:

Backend:

- Initialize FastAPI project
- Setup virtual environment
- Setup dependency management
- Create configuration system
- Add environment variables

Frontend:

- Initialize Next.js application
- Setup TypeScript
- Setup Tailwind
- Setup component library


Infrastructure:

Create:

docker-compose.yml


Services:

- frontend
- backend
- postgres
- redis
- neo4j


Deliverable:

Application starts successfully.


---

# Phase 1 — Basic RAG MVP

Goal:

Create a working AI knowledge assistant.

Do NOT build agents yet.


## Backend Tasks

Implement document ingestion.

Supported:

- PDF upload
- TXT upload
- Markdown upload


Pipeline:

Document

↓

Parser

↓

Text cleaner

↓

Chunker

↓

Embedding generator

↓

PostgreSQL pgvector


Store:

Document:

- id
- filename
- metadata
- upload_time


Chunk:

- id
- document_id
- content
- embedding


---

## Retrieval

Implement:

Semantic similarity search.


Flow:

User question

↓

Embedding

↓

Vector search

↓

Top K chunks

↓

LLM response


Responses must include:

- answer
- source documents


---

## Frontend

Create:

Chat page

Features:

- Send questions
- Display responses
- Show citations


Document page:

- Upload files
- View uploaded documents


---

## Phase 1 Success Criteria

A user can:

1. Upload a PDF
2. Ask questions
3. Receive accurate answers
4. See referenced sources


---

# Phase 2 — Agent Architecture

Goal:

Replace simple RAG chain with LangGraph agent.


Create:

knowledge_agent.py


Agent state:

AgentState:
query
retrieved_documents
graph_context
answer
sources


Create tools:

## Search Tool

Purpose:

Search user documents.


## Summarization Tool

Purpose:

Generate summaries.


## Memory Tool

Purpose:

Store new knowledge.


## Graph Search Tool

Purpose:

Find related concepts.


Agent workflow:

User Query
↓
Query Analyzer
↓
Decision Node
↓
Tool Selection
↓
Retrieval
↓
Reasoning
↓
Response Generation
↓
Citation Validation


---

# Phase 3 — Knowledge Graph

Goal:

Build structured knowledge representation.


Implement entity extraction.


Example:


Input:

"React is a JavaScript library created by Meta."


Extract:


Entities:

React

JavaScript

Meta


Relationships:


React
|
uses
|
JavaScript


React
|
created_by
|
Meta


Store in Neo4j.


---

## Graph Features

Users can:

- View graph
- Expand nodes
- Search concepts
- Ask questions about relationships


Frontend:

Use React Flow.


---

# Phase 4 — Advanced Retrieval

Goal:

Create a high-quality RAG system.


Implement:

## Hybrid Search

Combine:

1. Vector search
2. Keyword search
3. Graph traversal


Ranking:

Results
↓
Reranker
↓
Top Context
↓
LLM


Add:

- query rewriting
- multi-hop reasoning
- context compression


---

# Phase 5 — Evaluation System

Goal:

Prove system quality.


Implement evaluation dashboard.


Metrics:

Retrieval:

- Precision@K
- Recall@K


Generation:

- Answer relevance
- Citation correctness
- Hallucination detection


Tools:

- RAGAS
- LangSmith


Store evaluation history.


---

# Phase 6 — Production Features


Add:


## Authentication

Use:

- Auth.js
- Clerk


## User Data Isolation

Every user has:

- private documents
- private graph
- private conversations


## Deployment

Frontend:

Vercel


Backend:

AWS / Railway


Database:

Managed PostgreSQL


---

# Coding Rules

Follow these rules strictly.


## 1. Build Incrementally

Never implement future phases early.


Complete:

Phase 1

before:

Phase 2


---

## 2. Write Maintainable Code

Requirements:

- Small functions
- Clear naming
- Type hints
- Documentation
- Error handling


Avoid:

- giant files
- duplicated logic
- hardcoded values


---

## 3. Testing

Every important module needs tests.


Minimum:

Ingestion:

- parser tests
- chunking tests


Retrieval:

- search tests


Agent:

- tool execution tests


---

## 4. Documentation

Maintain:

README.md


Include:

- architecture diagram
- setup instructions
- environment variables
- screenshots
- design decisions


---

## 5. Git Workflow

Commit frequently.

Use commits:

feat: implement pdf ingestion pipeline
feat: add vector retrieval
feat: create langgraph agent
feat: add knowledge graph extraction
test: add retrieval tests


---

# Final Resume Requirements

The final project should demonstrate:


Technical:

✅ LangGraph agent  
✅ RAG pipeline  
✅ Vector database  
✅ Knowledge graph  
✅ Tool calling  
✅ Hybrid retrieval  
✅ Evaluation metrics  
✅ Full-stack deployment  


Product:

✅ Clean UX  
✅ Real user problem  
✅ Scalable architecture  
✅ Good documentation  

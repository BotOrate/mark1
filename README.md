# BotOrate

## Introduction

**BotOrate** is an advanced AI-powered assistant designed to enhance user interaction with product data through a multi-agent workflow system. The chatbot leverages product metadata and customer reviews to provide rich, context-aware answers to user queries.

BotOrate is designed for **local deployment** and features a **Streamlit** web interface. It integrates **Elasticsearch** to efficiently handle product name and feature searches, supporting semantic retrieval over user reviews and metadata.

Multiple LLMs power its backend operations:
- **GPT-4o-Mini** for query routing (Supervisor Module)
- **LLaMA 3.1-8B** for metadata summarization
- **LLaMA 3.1-70B** for final response synthesis

LangGraph orchestrates these agents, Langfuse traces all interactions and logs feedback, and MLflow tracks experiments and model versions.

## System Highlights
- **Multi-Agent LangGraph Workflow**
- **Metadata and Review Based Contextual Responses**
- **Streamlit Frontend** for User Interaction
- **Elasticsearch** for Fast Semantic Search
- **MLflow + Langfuse** for Experiment Tracking & Analytics
- **CI/CD** via GitHub Actions

## Installation and Setup

### Prerequisites
- Python >= 3.12
- [Poetry](https://python-poetry.org/docs/#installation) package manager

### Steps

1. **Clone the Repository**
```bash
git clone https://github.com/eCom-dev5/eCom-Chatbot.git
cd eCom-Chatbot
```

2. **Install Dependencies**
```bash
poetry config virtualenvs.in-project true
poetry install
```

3. **Create .env File**
```bash
touch .env
```
Fill in the following environment variables:
```
OPENAI_API_KEY=<your-key>
HF_TOKEN=<your-token>
GROQ_API_KEY=<your-key>
LANGFUSE_SECRET_KEY=<key>
LANGFUSE_PUBLIC_KEY=<key>
LANGFUSE_HOST=<host>
VERTA_API_ACCESS_TOKEN=<uuid or string>
HOST=0.0.0.0
PORT=80
DB_USER=<username>
DB_PASS=<password>
DB_NAME=<db>
INSTANCE_CONNECTION_NAME=<string>
GOOGLE_APPLICATION_CREDENTIALS=./verta-gcp.json
MLFLOW_TRACKING_URI=<mlflow-uri>
MLFLOW_TRACKING_USERNAME=<dagshub-username>
MLFLOW_TRACKING_PASSWORD=<dagshub-token>
MS_TEAMS_WEBHOOK_URL=<optional>
```

4. **Configure Elasticsearch (Optional)**
Ensure your local Elasticsearch instance is running. The integration code should point to your local server.

5. **Run Data Pipelines**
```bash
cd data_pipeline
# Follow README here for setting up DB schema and data load
```

6. **Run the ML Pipelines**
To run the full 5-stage pipeline:
```bash
dvc repro
```
Or to run individual stages:
```bash
poetry run python src/main.py
```
Skip stages in `src/main.py` to test specific steps.

7. **Run Unit Tests**
```bash
poetry run pytest tests/test.py -v
```

8. **Start Local API (Optional)**
```bash
poetry run python src/serve.py
```
Open [http://0.0.0.0:80/docs](http://0.0.0.0:80/docs) to test endpoints.

9. **Launch Streamlit Interface**
```bash
poetry run streamlit run src/app.py
```
Interact with the chatbot via the web UI.

## Core Features

### 1. Metadata Summarizer
- Uses LLaMA 3.1-8B to convert product specs into readable summaries.

### 2. Vectorstore Retriever
- Uses FAISS + MiniLM + Elasticsearch to search and retrieve relevant reviews.

### 3. Supervisor Module
- Routes user query to metadata or vector-based pipeline (GPT-4o Mini).

### 4. Main LLM
- Synthesizes final answer using LLaMA 3.1-70B.

### 5. Feedback & Logging
- Logs session via Langfuse
- User feedback stored with `/score` endpoint.

### 6. Evaluation & Bias Detection
- Run with:
```bash
python src/pipeline/stage_03_model_evaluation.py
python src/pipeline/stage_04_bias_detection.py
```
- Logs to MLflow.

## Folder Structure
Refer to [FOLDER_STRUCTURE.md](readme/FOLDER_STRUCTURE.md) for an overview of files and directory layout.

## ML Pipelines
Detailed guides for each stage:
- [Prepare Base Model](readme/01_BASE_MODEL.md)
- [Test Ingestion](readme/02_TEST_INGESTION.md)
- [Model Evaluation](readme/03_MODEL_EVALUATION.md)
- [Bias Detection](readme/04_BIAS_DETECTION.md)

## CI/CD
Refer to [CICD_WORKFLOW.MD](readme/CICD_WORKFLOW.MD) for instructions on using GitHub Actions for testing & deployment.



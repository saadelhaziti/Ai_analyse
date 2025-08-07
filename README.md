# Retail Chatbot & Data API Project

This project is a FastAPI-based backend for retail data analysis and chatbot interactions. It includes:
- Chatbot API endpoints for conversation and Q&A
- Data visualization and CSV analysis
- Integration with external services (Ollama, ElasticSearch, Minio)
- Docker support for easy deployment

## Features
- Chatbot endpoints for retail Q&A
- CSV and SQL prompt analysis
- Data storage and retrieval
- RESTful API structure
- Ready for containerization

## Project Structure
```
├── chatbot/           # Chatbot API logic
├── DB_Save/           # Data storage APIs (ElasticSearch, Minio)
├── llm_engine/        # Prompt templates and loaders
├── Models/            # Data models and schemas
├── retail_db/         # Sample retail database CSVs
├── Visualizer_csv/    # CSV visualization endpoints
├── Visualizer_DB/     # DB visualization endpoints
├── main.py            # FastAPI app entrypoint
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker build instructions
├── docker-compose.yml # (optional) Multi-service orchestration
```

## Getting Started

### 1. Clone the Repository
```powershell
git clone https://github.com/yourusername/retail-chatbot-api.git
cd retail-chatbot-api
```

### 2. Install Python Requirements
Make sure you have Python 3.11+ installed.
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the App Locally
```powershell
uvicorn main:app --reload
```
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

### 4. Build & Run with Docker
#### Build the Docker image
```powershell
docker build -t retail-chatbot-api .
```


####  Using Docker Compose
If you have a `docker-compose.yml` for multi-service setup:
```powershell
docker-compose up --build
```

### 5. Environment Variables
- The chatbot connects to Ollama at `http://ollama:11434` (for Docker on Windows).
- Configure other service endpoints as needed in your code or via environment variables.


### 6. MinIO Bucket Setup for Testing
You need to create a bucket in MinIO named `test1` for the tests to run properly.
This can be done via the MinIO web interface or using the MinIO client (`mc`).

Example using MinIO client:
```powershell
mc mb myminio/test1
```
Replace `myminio` with your MinIO alias if different.
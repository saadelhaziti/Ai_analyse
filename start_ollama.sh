#!/bin/sh

# Start Ollama in background
ollama serve &

# Wait for API to be ready
until curl -s http://localhost:11434/api/tags > /dev/null; 
do
  echo "Waiting for Ollama to start..."
  sleep 3
done

# Pull the model
ollama pull mistral:7b > /dev/null 2>&1
echo "Model 'mistral:7b' pulled successfully."
# Keep container running in foreground
tail -f /dev/null

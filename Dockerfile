FROM python:3.11.9-slim-bookworm

# System dependencies (only if you use pandas, numpy, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libjpeg-dev \
    curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy only requirements first (use Docker cache smartly)
COPY requirements.txt .

# Upgrade pip and install dependencies using binary (faster)
RUN pip install --upgrade pip && \
    pip install --prefer-binary --no-cache-dir -r requirements.txt

# Now copy rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

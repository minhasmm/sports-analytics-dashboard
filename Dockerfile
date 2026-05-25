FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY backend/ /app/backend/
COPY data/ /app/data/

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "backend.app:app"]

# --------------------------------------------------
# Base Image
# --------------------------------------------------
FROM python:3.10-slim

# --------------------------------------------------
# Environment Variables
# --------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --------------------------------------------------
# System Dependencies (Java for Spark)
# --------------------------------------------------
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# --------------------------------------------------
# Working Directory
# --------------------------------------------------
WORKDIR /app

# --------------------------------------------------
# Python Dependencies
# --------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------------
# Copy Project Files
# --------------------------------------------------
COPY src ./src
COPY scripts ./scripts
COPY data ./data

# --------------------------------------------------
# Default Command
# --------------------------------------------------
CMD ["python", "scripts/run_pipeline.py"]

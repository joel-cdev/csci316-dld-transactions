# --------------------------------------------------
# Base Image
# --------------------------------------------------
FROM python:3.10-slim-bookworm

# --------------------------------------------------
# Environment Variables
# --------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --------------------------------------------------
# System Dependencies (Java for Spark)
# --------------------------------------------------

FROM eclipse-temurin:21-jre-jammy

RUN apt-get update && apt-get install -y --fix-missing \
    python3 python3-pip curl \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk
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

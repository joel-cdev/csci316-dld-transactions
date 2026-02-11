# --------------------------------------------------
# Base Image
# --------------------------------------------------
FROM python:3.11-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# --------------------------------------------------
# Install system dependencies
# --------------------------------------------------
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk-headless \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Set Java environment (required for PySpark)
# --------------------------------------------------
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV PATH="$JAVA_HOME/bin:$PATH"

# --------------------------------------------------
# Set working directory
# --------------------------------------------------
WORKDIR /app

# --------------------------------------------------
# Copy requirements first (for caching)
# --------------------------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------------
# Copy project files
# --------------------------------------------------
COPY . .

# --------------------------------------------------
# Expose Streamlit port
# --------------------------------------------------
EXPOSE 8501

# --------------------------------------------------
# Default command: launch Streamlit
# --------------------------------------------------
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]

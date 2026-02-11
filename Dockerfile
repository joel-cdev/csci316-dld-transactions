FROM python:3.10-slim

WORKDIR /app

# Copy only what Streamlit needs
COPY streamlit_app.py .
COPY data/outputs ./data/outputs
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]

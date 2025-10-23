FROM python:3.10-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of app files
COPY . .

# Expose both backend (FastAPI) and frontend (Streamlit)
EXPOSE 8000 8501

# Run FastAPI backend & Streamlit frontend together
CMD uvicorn app:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0

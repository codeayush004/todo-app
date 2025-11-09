FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000 8501

CMD uvicorn app:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0

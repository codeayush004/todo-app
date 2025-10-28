from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# ✅ Attach Prometheus instrumentation immediately before startup
Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {"message": "Todo App API is running"}

@app.get("/todos")
def get_todos():
    return {"todos": ["task1", "task2"]}

@app.post("/todos")
def add_todo():
    return {"message": "Todo added successfully"}

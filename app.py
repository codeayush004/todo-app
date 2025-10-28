from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Todo backend is running"}

@app.get("/todos")
def get_todos():
    return {"todos": ["Task 1", "Task 2"]}

@app.post("/todos")
def add_todo():
    return {"message": "Todo added"}

# ✅ Initialize Prometheus metrics
@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

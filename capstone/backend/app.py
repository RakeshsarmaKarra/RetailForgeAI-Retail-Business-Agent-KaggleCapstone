from fastapi import FastAPI
from .routes_agent import router as agent_router
from .routes_metrics import router as metrics_router
from .routes_eval import router as eval_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "RetailForgeAI",
        "status": "running"
    }

app.include_router(agent_router)
app.include_router(metrics_router)
app.include_router(eval_router)


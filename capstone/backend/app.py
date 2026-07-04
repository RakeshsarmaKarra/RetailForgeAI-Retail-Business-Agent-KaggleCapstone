from fastapi import FastAPI
from backend.routes_agent import router as agent_router
from backend.routes_metrics import router as metrics_router
from backend.routes_eval import router as eval_router

app = FastAPI()

app.include_router(agent_router)
app.include_router(metrics_router)
app.include_router(eval_router)

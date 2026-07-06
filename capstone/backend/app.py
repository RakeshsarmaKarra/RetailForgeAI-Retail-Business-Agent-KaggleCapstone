# from fastapi import FastAPI
# from .routes_agent import router as agent_router
# from .routes_metrics import router as metrics_router
# from .routes_eval import router as eval_router

# app = FastAPI()

# @app.get("/")
# def home():
#     return {
#         "project": "RetailForgeAI",
#         "status": "running"
#     }

# app.include_router(agent_router)
# app.include_router(metrics_router)
# app.include_router(eval_router)

# New added
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes_agent import router as agent_router
from .routes_metrics import router as metrics_router
from .routes_eval import router as eval_router
from .routes_forecast import router as forecast_router

app = FastAPI(
    title="RetailForgeAI",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "project": "RetailForgeAI",
        "status": "running"
    }


app.include_router(agent_router)
app.include_router(metrics_router)
app.include_router(eval_router)
app.include_router(forecast_router)
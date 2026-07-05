from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics/health")
def metrics_health():
    return {
        "status": "ok",
        "module": "metrics"
    }
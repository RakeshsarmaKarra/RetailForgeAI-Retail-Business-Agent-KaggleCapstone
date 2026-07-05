from fastapi import APIRouter
from pydantic import BaseModel

from .sql_guardrails import (
    is_select_only,
    uses_whitelisted_views,
    apply_row_limit
)

router = APIRouter()


class EvalRequest(BaseModel):
    sql: str


@router.post("/eval/sql")
def evaluate_sql(request: EvalRequest):

    sql = request.sql

    select_check = is_select_only(sql)
    whitelist_check = uses_whitelisted_views(sql)

    safe_sql = apply_row_limit(sql, max_rows=100)

    return {
        "evaluation": {
            "select_only": select_check,
            "whitelisted_view": whitelist_check,
            "row_limit_applied": True
        },
        "overall_status": (
            "PASS"
            if select_check and whitelist_check
            else "FAIL"
        ),
        "original_sql": sql,
        "safe_sql": safe_sql
    }


@router.get("/eval/health")
def eval_health():
    return {
        "status": "ok",
        "module": "evaluation"
    }

from fastapi import APIRouter
from pydantic import BaseModel
from .sql_guardrails import is_select_only, uses_whitelisted_views, apply_row_limit
from .genai_client import generate_sql

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/agent/query")
def agent_query(request: QueryRequest):

    question = request.question

    generated_sql = generate_sql(question)

    if not is_select_only(generated_sql):
        return {
            "status": "refused",
            "reason": "Only SELECT queries are allowed.",
            "question": question,
            "generated_sql": generated_sql,
        }

    if not uses_whitelisted_views(generated_sql):
        return {
            "status": "refused",
            "reason": "Query must use approved views (e.g., vw_category_revenue).",
            "question": question,
            "generated_sql": generated_sql,
        }

    safe_sql = apply_row_limit(generated_sql, max_rows=100)

    return {
        "status": "ok",
        "question": question,
        "generated_sql": safe_sql,
    }
import time
from .llm_logger import log_agent_event


from fastapi import APIRouter
from pydantic import BaseModel

from .sql_guardrails import (
    is_select_only,
    uses_whitelisted_views,
    apply_row_limit
)

from .genai_client import generate_sql
from .query_executor import execute_query
from .insight_generator import generate_insight

router = APIRouter()


class QueryRequest(BaseModel):
    question: str


@router.post("/agent/query")
def agent_query(request: QueryRequest):
    start_time = time.time()

    question = request.question

    # Step 1: Generate SQL
    generated_sql = generate_sql(question)

    # Step 2: Guardrail - SELECT only
    if not is_select_only(generated_sql):
        return {
            "status": "refused",
            "reason": "Only SELECT queries are allowed.",
            "question": question,
            "generated_sql": generated_sql
        }

    # Step 3: Guardrail - approved views only
    if not uses_whitelisted_views(generated_sql):
        return {
            "status": "refused",
            "reason": "Query must use approved views.",
            "question": question,
            "generated_sql": generated_sql
        }

    # Step 4: Apply row limit
    safe_sql = apply_row_limit(
        generated_sql,
        max_rows=100
    )

    # Step 5: Execute query
    results = execute_query(safe_sql)

    # Step 6: Generate business insight
    insight = generate_insight(
        question,
        results
    )

    # Calculate latency
    latency_ms = round((time.time() - start_time) * 1000, 2)

# Log event
    log_agent_event(
        question=question,
        generated_sql=safe_sql,
        status="ok",
        latency_ms=latency_ms,
        rows_returned=len(results)
    )

# Return response
    return {
        "status": "ok",
        "question": question,
        "generated_sql": safe_sql,
        "results": results,
        "insight": insight,
        "rows_returned": len(results)
    }
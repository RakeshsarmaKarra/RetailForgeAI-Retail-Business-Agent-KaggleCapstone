print("LOGGER LOADED")
import json
import time
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parents[1] / "logs" / "agent_logs.jsonl"

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log_agent_event(
    question,
    generated_sql,
    status,
    latency_ms,
    rows_returned=0,
    error=None
):
    event = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "question": question,
        "generated_sql": generated_sql,
        "status": status,
        "latency_ms": latency_ms,
        "rows_returned": rows_returned,
        "error": error
    }

    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
import json
import time
import requests
from pathlib import Path

# Adjust if your backend runs elsewhere
BACKEND_URL = "http://localhost:8000/agent/query"

BASE_DIR = Path(__file__).resolve().parent
TESTS_FILE = BASE_DIR / "tests.json"
RESULTS_FILE = BASE_DIR / "results.csv"


def load_tests():
    with open(TESTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def run_single_test(test):
    question = test["question"]
    expected_view = test.get("expected_view")
    expected_status = test.get("expected_status")

    start = time.time()
    resp = requests.post(
        BACKEND_URL,
        json={"question": question},
        timeout=15,  # simple timeout guardrail
    )
    latency_ms = (time.time() - start) * 1000

    data = resp.json()

    status = data.get("status")
    generated_sql = data.get("generated_sql", "") or ""
    reason = data.get("reason", "")

    # Simple checks
    uses_expected_view = (
        bool(expected_view)
        and expected_view.upper() in generated_sql.upper()
    )

    status_matches = (
        expected_status is None or status == expected_status
    )

    return {
        "id": test.get("id", ""),
        "bucket": test.get("bucket", ""),
        "question": question,
        "status": status,
        "status_matches": status_matches,
        "reason": reason,
        "generated_sql": generated_sql,
        "uses_expected_view": uses_expected_view,
        "latency_ms": round(latency_ms, 2),
    }


def write_results(rows):
    # Simple CSV for later analysis
    headers = [
        "id",
        "bucket",
        "question",
        "status",
        "status_matches",
        "reason",
        "generated_sql",
        "uses_expected_view",
        "latency_ms",
    ]
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write(",".join(headers) + "\n")
        for row in rows:
            values = [str(row.get(h, "")).replace("\n", " ") for h in headers]
            f.write(",".join(values) + "\n")


def main():
    tests = load_tests()
    results = []

    for test in tests:
        result = run_single_test(test)
        print(
            f"[{result['id']}] bucket={result['bucket']} "
            f"status={result['status']} latency={result['latency_ms']}ms "
            f"uses_expected_view={result['uses_expected_view']}"
        )
        results.append(result)

    write_results(results)
    print(f"\nSaved results to {RESULTS_FILE}")


if __name__ == "__main__":
    main()
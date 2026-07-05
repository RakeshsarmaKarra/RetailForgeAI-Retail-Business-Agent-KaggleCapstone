
FORBIDDEN_KEYWORDS = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE"]

def is_select_only(sql: str) -> bool:
    sql_upper = sql.strip().upper()
    if not sql_upper.startswith("SELECT"):
        return False
    return not any(keyword in sql_upper for keyword in FORBIDDEN_KEYWORDS)

    
ALLOWED_VIEWS = ["VW_CATEGORY_REVENUE"]  # add more later

def uses_whitelisted_views(sql: str) -> bool:
    sql_upper = sql.upper()
    # Ensure at least one allowed view appears
    if not any(view in sql_upper for view in ALLOWED_VIEWS):
        return False
    # Optionally: ban raw table names if you define them
    # e.g., if "RETAIL_TRANSACTIONS" in sql_upper: return False
    return True

def apply_row_limit(sql: str, max_rows: int = 100) -> str:
    sql_upper = sql.upper()
    if "LIMIT" in sql_upper:
        return sql  # already limited
    return sql.rstrip(" ;") + f" LIMIT {max_rows};"
from google import genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def generate_sql(question: str):

    prompt = f"""
You are a retail business SQL expert.

Convert the user question into SQL.

Rules:
- Only generate SELECT statements.
- Use approved views:
    vw_category_revenue
    vw_inventory_risk
    vw_campaign_performance
- Return SQL only.
- Do NOT use markdown.
- Do NOT wrap SQL in triple backticks.

Question:
{question}
"""

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )

    sql = response.text.strip()
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql
    
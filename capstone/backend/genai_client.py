from google import genai
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

# Cache
question_cache = {}

# Only create Gemini client if API key exists
client = None
if API_KEY:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception:
        client = None


def generate_sql(question: str) -> str:

    # -----------------------------
    # Check cache first
    # -----------------------------
    if question in question_cache:
        print("Returning SQL from cache")
        return question_cache[question]

    q = question.lower()

    # -----------------------------
    # Local mappings (NO Gemini)
    # -----------------------------
    if "revenue" in q and "category" in q:

        sql = """
        SELECT
            category_name,
            total_revenue
        FROM
            vw_category_revenue
        LIMIT 100
        """

        question_cache[question] = sql
        return sql

    if "campaign" in q:

        sql = """
        SELECT *
        FROM
            vw_campaign_performance
        LIMIT 100
        """

        question_cache[question] = sql
        return sql

    if "inventory" in q:

        sql = """
        SELECT *
        FROM
            vw_inventory_risk
        LIMIT 100
        """

        question_cache[question] = sql
        return sql

    # -----------------------------
    # Fallback to Gemini
    # -----------------------------
    if client:

        prompt = f"""
        You are a Retail SQL Assistant.

        User question:
        {question}

        Rules:
        - Generate SELECT statements only
        - Use approved views only:
            vw_category_revenue
            vw_inventory_risk
            vw_campaign_performance
        - Return SQL only
        """

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            sql = response.text.strip()

            question_cache[question] = sql

            return sql

        except Exception as e:

            print("Gemini Error:", e)

    # -----------------------------
    # Final fallback
    # -----------------------------
    sql = """
    SELECT
        category_name,
        total_revenue
    FROM
        vw_category_revenue
    LIMIT 100
    """

    question_cache[question] = sql

    return sql
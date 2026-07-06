from capstone.backend.genai_client import client


def generate_insight(question: str, results) -> str:
    """
    Turn the question and SQL results into a concise retail business insight.
    """

    prompt = f"""
You are a Retail Business Analyst.

User question:
{question}

SQL result rows:
{results}

Using the data above, write a concise, business-friendly insight.
Focus on what is happening (trends, comparisons) and what it means
for the retail business. Avoid SQL or technical language.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    insight = response.text.strip()
    return insight
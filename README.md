# Agent Name: RetailForgeAI

![Image](https://github.com/RakeshsarmaKarra/RetailForgeAI-Retail-Business-Agent-KaggleCapstone/blob/main/AI%20Agent.png)

## Overview
A Walmart-inspired enterprise AI agent for retail sales, inventory monitoring, campaign tracking, and business Q&A using trusted database queries.

## Business Problem
Retail teams often need fast answers about revenue, stock levels, and campaign effectiveness, but data is spread across systems.

## Features
- Sales and revenue dashboard
- Inventory monitoring and stock risk alerts
- Campaign and discount performance tracking
- AI assistant with database-grounded responses
- LLMOps evaluation and prompt/version tracking

## Architecture
![Insert architecture diagram](https://github.com/RakeshsarmaKarra/RetailForgeAI-Retail-Business-Agent-KaggleCapstone/blob/main/Flowchart.png)

## Tech Stack
- Python
- FastAPI / Streamlit
- PostgreSQL / SQLite
- LLM framework
- SQL + evaluation pipeline

## Repo Structure

```text
capstone/
├── backend/                    # Backend APIs, business logic, forecasting, SQL guardrails
│   ├── __pycache__/            # Python cache files
│   ├── app.py                  # Main backend application entry point
│   ├── forecasting.py          # Forecasting logic
│   ├── genai_client.py         # LLM / GenAI integration
│   ├── insight_generator.py    # Insight generation
│   ├── llm_logger.py           # LLM logging
│   ├── query_executor.py       # SQL execution
│   ├── routes_agent.py         # Agent routes
│   ├── routes_eval.py          # Evaluation routes
│   ├── routes_forecast.py      # Forecast routes
│   ├── routes_metrics.py       # Metrics routes
│   └── sql_guardrails.py       # SQL safety checks
├── data/                       # Retail datasets
├── eval/                       # Evaluation files
├── frontend/
│   └── index.html              # Frontend UI
├── mcp/                        # MCP files
├── prompts/
│   ├── guardrail_refusal.md    # Refusal prompt
│   ├── insight_summarization.md# Summarization prompt
│   ├── intent_classification.md# Intent classification prompt
│   └── sql_generation.md       # SQL generation prompt
├── skills/                     # Skills/capabilities
├── spec/                       # Specifications and planning docs
└── sql/                        # SQL scripts and assets
```


## Setup
1. Clone repo
2. Create virtual environment
3. Install requirements
4. Add `.env`
5. Run database setup
6. Start app

## Example Questions
- Which categories generated the highest revenue this week?

![revenue](https://github.com/RakeshsarmaKarra/RetailForgeAI-Retail-Business-Agent-KaggleCapstone/blob/main/Agent%20Dashboard.jpg)

- Which products are at stockout risk?

![Product](https://github.com/RakeshsarmaKarra/RetailForgeAI-Retail-Business-Agent-KaggleCapstone/blob/main/Inventory.jpg)

- Did the current campaign increase new customers?

![campaigns](https://github.com/RakeshsarmaKarra/RetailForgeAI-Retail-Business-Agent-KaggleCapstone/blob/main/Campaigns.jpg)

## Evaluation
Explain golden dataset, SQL accuracy, answer faithfulness, and guardrails.

## Limitations
Prototype data and simulated business environment.

## Future Improvements
Add forecasting, agent actions, and production monitoring.

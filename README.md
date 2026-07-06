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

The project is evaluated using a set of retail business questions covering sales, inventory, and campaign analysis. Evaluation focuses on SQL correctness, business answer faithfulness, guardrail behavior, and whether responses remain grounded in approved database views.

## Limitations

This project currently uses a prototype retail environment with simulated or sample business data rather than a live enterprise retail system. Forecasting and campaign measurement are implemented as proof-of-concept components and can be extended further with production-scale datasets and stronger monitoring.

## Future Improvements

Future work includes live warehouse integration, more advanced demand forecasting, role-based access control, explainable recommendations, and production-grade observability for agent prompts, queries, latency, and business outcomes.

## Capstone Context

This repository was developed for the Kaggle × Google 5-Day AI Agents: Intensive Vibe Coding Capstone. The goal of the project is to demonstrate how AI agents can solve real business problems in retail through a combination of dashboards, grounded SQL retrieval, forecasting, and LLMOps practices.

## License
This project is licensed under the Apache-2.0 License.

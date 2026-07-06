# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/metrics/health")
# def metrics_health():
#     return {
#         "status": "ok",
#         "module": "metrics"
#     }

# New added
from fastapi import APIRouter, Query
from datetime import datetime
from .query_executor import get_revenue_by_category
from .forecasting import forecast_category_demand

router = APIRouter()


@router.get("/metrics/dashboard")
def dashboard_metrics(
    category: str = Query(default="All Categories"),
    channel: str = Query(default="All Channels"),
    date_range: str = Query(default="Last 30 Days")
):

    categories = get_revenue_by_category()
    

    # Category filtering
    if category != "All Categories":
        categories = [
            item
            for item in categories
            if item["category"] == category
        ]

    return {
        "total_revenue": 1250000,
        "total_sales": 24580,
        "profit_margin": 18.2,
        "total_customers": 12300,
        "selected_category": category,
        "selected_channel": channel,
        "selected_date_range": date_range,
        "revenue_by_category": categories,
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@router.get("/metrics/inventory")
def inventory_metrics():
    return {
        "inventory": [
            {"sku": "TV001", "product": "Smart TV", "current_stock": 50, "predicted_demand": 120, "status": "Reorder Needed"},
            {"sku": "PH001", "product": "Smartphone", "current_stock": 300, "predicted_demand": 220, "status": "Healthy"},
            {"sku": "LP001", "product": "Laptop", "current_stock": 10, "predicted_demand": 90, "status": "Low Stock"}
        ]
    }


@router.get("/metrics/campaigns")
def campaign_metrics():
    return {
        "campaigns": [
            {"name": "Summer Sale", "discount": "15%", "revenue_lift": "18%", "new_customers": 250, "conversion_lift": "12%"},
            {"name": "Electronics Weekend", "discount": "10%", "revenue_lift": "22%", "new_customers": 180, "conversion_lift": "15%"},
            {"name": "Grocery Rewards", "discount": "5%", "revenue_lift": "9%", "new_customers": 320, "conversion_lift": "8%"}
        ]
    }


@router.get("/metrics/health")
def metrics_health():
    return {
        "status": "ok",
        "module": "metrics"
    }

@router.get("/metrics/forecast")
def demand_forecast():

    return {
        "forecast": forecast_category_demand()
    }
from fastapi import APIRouter
from .forecasting import forecast_category_demand

router = APIRouter()


@router.get("/forecast/category-demand")
def category_forecast():

    forecast = forecast_category_demand()

    return {
        "forecast": forecast
    }
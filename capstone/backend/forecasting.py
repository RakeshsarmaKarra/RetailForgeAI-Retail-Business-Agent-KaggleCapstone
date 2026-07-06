import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data" / "Retail_Transaction_Dataset.xlsx"

df = pd.read_excel(DATA_PATH)


def forecast_category_demand():
    df_copy = df.copy()

    df_copy["TransactionDate"] = pd.to_datetime(df_copy["TransactionDate"])

    forecasts = []

    for category in df_copy["ProductCategory"].unique():
        temp = (
            df_copy[df_copy["ProductCategory"] == category]
            .groupby(df_copy["TransactionDate"].dt.to_period("M"))["Quantity"]
            .sum()
            .reset_index()
        )

        temp["month_number"] = np.arange(len(temp))

        if len(temp) < 2:
            continue

        X = temp[["month_number"]]
        y = temp["Quantity"]

        model = LinearRegression()
        model.fit(X, y)

        next_month = np.array([[len(temp)]])
        prediction = model.predict(next_month)[0]

        forecasts.append({
            "category": category,
            "forecast_quantity": int(round(prediction))
        })

    return forecasts


if __name__ == "__main__":
    print(forecast_category_demand())
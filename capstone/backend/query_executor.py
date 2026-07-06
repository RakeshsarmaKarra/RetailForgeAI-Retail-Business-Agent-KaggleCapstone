import pandas as pd

DATA_PATH = "capstone/data/Retail_Transaction_Dataset.xlsx"

# Load data once when application starts
df = pd.read_excel(DATA_PATH)


def execute_query(sql: str):

    sql = sql.lower()

    # Revenue by category
    if "category" in sql and "revenue" in sql:

        result = (
            df.groupby("ProductCategory")
            ["TotalAmount"]
            .sum()
            .reset_index()
            .rename(
                columns={
                    "ProductCategory": "category",
                    "TotalAmount": "revenue"
                }
            )
            .sort_values(
                by="revenue",
                ascending=False
            )
        )

        return result.to_dict(orient="records")

    # Revenue by payment method
    if "payment" in sql:

        result = (
            df.groupby("PaymentMethod")
            ["TotalAmount"]
            .sum()
            .reset_index()
            .rename(
                columns={
                    "PaymentMethod": "payment_method",
                    "TotalAmount": "revenue"
                }
            )
        )

        return result.to_dict(orient="records")

    # Revenue by store location
    if "location" in sql or "store" in sql:

        result = (
            df.groupby("StoreLocation")
            ["TotalAmount"]
            .sum()
            .reset_index()
            .rename(
                columns={
                    "StoreLocation": "store_location",
                    "TotalAmount": "revenue"
                }
            )
        )

        return result.to_dict(orient="records")

    # Total sales summary
    if "total sales" in sql or "total revenue" in sql:

        return [{
            "total_revenue": float(df["TotalAmount"].sum()),
            "total_transactions": int(len(df))
        }]

    return []

def get_revenue_by_category():

    result = (
        df.groupby("ProductCategory")
        ["TotalAmount"]
        .sum()
        .reset_index()
        .rename(
            columns={
                "ProductCategory": "category",
                "TotalAmount": "revenue"
            }
        )
        .sort_values(
            by="revenue",
            ascending=False
        )
    )

    return result.to_dict(orient="records")

if __name__ == "__main__":
    print(get_revenue_by_category())
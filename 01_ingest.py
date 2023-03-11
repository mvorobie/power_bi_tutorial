import sqlite3

import pandas as pd
from pathlib import Path

CAR_SALES_PATH = Path("C:/Users/vmish/PycharmProjects/power_bi_tutorial/car_sales.db")

with sqlite3.connect(CAR_SALES_PATH) as connection:
    df = pd.read_sql_query("SELECT * FROM sales", connection)

cars = df[
    [
        "vin",
        "car",
        "mileage",
        "license",
        "color",
        "purchase_date",
        "purchase_price",
        "investment",
    ]
]
customers = df[["vin", "customer"]]
sales = df[["vin", "sale_price", "sale_date"]]

print(cars.head())
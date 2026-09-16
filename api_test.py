import requests
import pandas as pd

url = "https://api.frankfurter.dev/v2/rate/usd/eur"

response = requests.get(url)

data = response.json()

print("\n--- JSON Response ---")
print(data)

df = pd.DataFrame([data])

print("\n--- DataFrame ---")
print(df)

sales_data = pd.read_csv("sales_data.csv")

exchange_rate = data["rate"]

sales_data["amount_in_eur"] = sales_data["amount"] * exchange_rate

print("\n--- Sales Data With EUR Amount ---")
print(sales_data[["product", "amount", "amount_in_eur"]])
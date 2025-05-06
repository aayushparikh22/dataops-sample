import pandas as pd
import requests

def fetch_data():
    url = "https://api.example.com/sales"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("data/raw_sales.csv", index=False)

if __name__ == "__main__":
    fetch_data()

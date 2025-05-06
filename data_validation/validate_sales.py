import pandas as pd

def validate_data():
    df = pd.read_csv("data/raw_sales.csv")
    assert df.notnull().all().all(), "Missing values found!"

if __name__ == "__main__":
    validate_data()

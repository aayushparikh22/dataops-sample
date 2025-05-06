import pandas as pd
from sqlalchemy import create_engine

def store_data():
    df = pd.read_csv("data/raw_sales.csv")
    engine = create_engine("postgresql://user:password@localhost:5432/salesdb")
    df.to_sql("clean_sales", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    store_data()

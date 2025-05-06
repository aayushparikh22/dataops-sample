import os

os.system("python data_ingestion/fetch_data.py")
os.system("python data_validation/validate_sales.py")
os.system("python data_storage/store_data.py")

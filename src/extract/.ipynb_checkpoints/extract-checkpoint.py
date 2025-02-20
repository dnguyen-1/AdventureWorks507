#import packages
import requests
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine

def fetch_csv_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Convert the raw data into a pandas DataFrame (handling tab separation)
    data = pd.read_csv(StringIO(response.text), delimiter='\t', header=None)

    # Return cleaned data
    return data

# URL of the raw CSV file on GitHub
salesorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesOrderDetail.csv"
salesterritory_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesTerritory.csv"
purchaseorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderDetail.csv"
shipmethod_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/ShipMethod.csv"
employee_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/Employee.csv"

# Fetch Data
SalesOrderDetail = fetch_csv_from_github(salesorderdetail_csv)
SalesTerritory = fetch_csv_from_github(salesterritory_csv)
PurchaseOrderDetail = fetch_csv_from_github(purchaseorderdetail_csv)
ShipMethod = fetch_csv_from_github(shipmethod_csv)
Employee = fetch_csv_from_github(employee_csv)
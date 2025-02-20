import requests
import pandas as pd
from io import StringIO  # Import StringIO from the io module

def fetch_csv_from_github(url):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful

    # Convert the raw CSV data into a pandas DataFrame
    data = pd.read_csv(StringIO(response.text))
    return data

# URL of the raw CSV file on GitHub
podetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderDetail.csv"
customers_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/Customer.csv"
salesorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesOrderDetail.csv"
salesterritory_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesTerritory.csv"
purchaseorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderDetail.csv"
shipmethod_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/ShipMethod.csv"
employee_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/Employee.csv"

# Fetch and print the data
PurchaseOrderDetail = fetch_csv_from_github(podetail_csv)
Customer = fetch_csv_from_github(customers_csv)
SalesOrderDetail = fetch_csv_from_github(salesorderdetail_csv)
SalesTerritory = fetch_csv_from_github(salesterritory_csv)
PurchaseOrderDetail = fetch_csv_from_github(purchaseorderdetail_csv)
ShipMethod = fetch_csv_from_github(shipmethod_csv)
Employee = fetch_csv_from_github(employee_csv)
import pandas as pd
from sqlalchemy import create_engine, text
import pymysql  # To handle MySQL connection

# MySQL connection string
server = 'team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com'
database = 'AdventureSales'
username = 'Ads507'
password = 'Gabrielleo24'
connection_string = f'mysql+pymysql://{username}:{password}@{server}/{database}'

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(connection_string)

# Function to load data into MySQL without replacing headers
def load_data_to_mysql():
    try:
        with engine.connect() as conn:
            # Remove existing data without dropping the table
            conn.execute(text("DELETE FROM PurchaseOrderDetail"))
            conn.execute(text("DELETE FROM SalesOrderDetail"))
            conn.execute(text("DELETE FROM SalesTerritory"))
            conn.execute(text("DELETE FROM ShipMethod"))
            conn.execute(text("DELETE FROM Employee"))
            conn.execute(text("DELETE FROM PurchaseOrderHeader"))
            conn.commit()  # Commit the transaction

        # Explicitly set DataFrame column names to match the SQL table schema
        PurchaseOrderDetail.columns = [
            'PurchaseOrderID', 'PurchaseOrderDetailID', 'DueDate', 'OrderQty',
            'ProductID', 'UnitPrice', 'LineTotal', 'ReceivedQty', 'RejectQty',
            'StockedQty', 'ModifiedDate'
        ]

        SalesOrderDetail.columns = [
            'SalesOrderID', 'SalesOrderDetailID', 'CarrierTrackingNumber',
            'OrderQty', 'ProductID', 'SpecialOfferID', 'UnitPrice',
            'UnitDiscount', 'LineTotal', 'rowguid', 'ModifiedDate'
        ]

        SalesTerritory.columns = [
            'TerritoryID', 'Name', 'CountryRegionCode', 'Geo_Group', 'SalesYTD',
            'SalesLastYear', 'CostYTD', 'CostLastYear', 'rowguid', 'ModifiedDate'
        ]

        ShipMethod.columns = [
            'ShipMethodID', 'Name', 'ShipBase', 'ShipRate', 'rowguid', 'ModifiedDate'
        ]

        Employee.columns = [
            'BusinessEntityID', 'NationalIDNumber', 'LoginID', 'OrganizationNode',
            'OrganizationLevel', 'JobTitle', 'BirthDate', 'MaritalStatus', 'Gender',
            'HireDate', 'SalariedFlag', 'VacationHours', 'SickLeaveHours',
            'CurrentFlag', 'rowguid', 'ModifiedDate'
        ]

        PurchaseOrderHeader.columns = [
            'PurchaseOrderID', 'RevisionNumber', 'order_status', 'EmployeeID', 
            'VendorID', 'ShipMethodID', 'OrderDate', 'ShipDate', 'SubTotal', 
            'TaxAmt', 'Freight', 'TotalDue', 'ModifiedDate'
        ]


        # Append the new data (without replacing the table structure)
        PurchaseOrderDetail.to_sql('PurchaseOrderDetail', con=engine, if_exists='append', index=False)
        SalesOrderDetail.to_sql('SalesOrderDetail', con=engine, if_exists='append', index=False)
        SalesTerritory.to_sql('SalesTerritory', con=engine, if_exists='append', index=False)
        ShipMethod.to_sql('ShipMethod', con=engine, if_exists='append', index=False)
        Employee.to_sql('Employee', con=engine, if_exists='append', index=False)
        PurchaseOrderHeader.to_sql('PurchaseOrderHeader', con=engine, if_exists='append', index=False)

    except Exception as e:
        print(f"Error loading data: {e}")

# Call the function to load the data
load_data_to_mysql()
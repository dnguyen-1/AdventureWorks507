#Transform
import pandas as pd
# Assign column names to each DataFrame
PurchaseOrderDetail.columns = ['PurchaseOrderID', 'PurchaseOrderDetailID', 'DueDate', 'OrderQty',
            'ProductID', 'UnitPrice', 'LineTotal', 'ReceivedQty', 'RejectQty',
            'StockedQty', 'ModifiedDate']

SalesOrderDetail.columns = ['SalesOrderID', 'SalesOrderDetailID', 'CarrierTrackingNumber',
            'OrderQty', 'ProductID', 'SpecialOfferID', 'UnitPrice',
            'UnitDiscount', 'LineTotal', 'rowguid', 'ModifiedDate']

SalesTerritory.columns = ['TerritoryID', 'Name', 'CountryRegionCode', 'Geo_Group', 'SalesYTD',
            'SalesLastYear', 'CostYTD', 'CostLastYear', 'rowguid', 'ModifiedDate']

ShipMethod.columns = ['ShipMethodID', 'Name', 'ShipBase', 'ShipRate', 'rowguid', 'ModifiedDate']

Employee.columns = ['BusinessEntityID', 'NationalIDNumber', 'LoginID', 'OrganizationNode',
            'OrganizationLevel', 'JobTitle', 'BirthDate', 'MaritalStatus', 'Gender',
            'HireDate', 'SalariedFlag', 'VacationHours', 'SickLeaveHours',
            'CurrentFlag', 'rowguid', 'ModifiedDate']

PurchaseOrderHeader.columns = ['PurchaseOrderID', 'RevisionNumber', 'order_status', 'EmployeeID', 
            'VendorID', 'ShipMethodID', 'OrderDate', 'ShipDate', 'SubTotal', 
            'TaxAmt', 'Freight', 'TotalDue', 'ModifiedDate']

def clean_column_names(df):
    """Strip spaces and lowercase all column names."""
    df.columns = df.columns.str.strip().str.lower()
    return df

def transform_salesorderdetail(df):
    df = clean_column_names(df)
    df.fillna(0, inplace=True)  # Replace null values
    print("SalesOrderDetail transformed successfully.")
    return df

def transform_purchaseorderdetail(df):
    df = clean_column_names(df)
    df.fillna(0, inplace=True)
    print("PurchaseOrderDetail transformed successfully.")
    return df

def transform_shipmethod(df):
    df = clean_column_names(df)
    df.fillna(0, inplace=True)
    print("ShipMethod transformed successfully.")
    return df

def transform_employee(df):
    df = clean_column_names(df)
    df.fillna(0, inplace=True)
    print("Employee transformed successfully.")
    return df

def transform_purchaseorderheader(df):
    df = clean_column_names(df)
    df.fillna(0, inplace=True)
    print("PurchaseOrderHeader transformed successfully.")
    return df

def main():
    """Load raw data and apply transformations"""

    # URLs of raw data
    salesorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesOrderDetail.csv"
    salesterritory_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesTerritory.csv"
    purchaseorderdetail_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderDetail.csv"
    shipmethod_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/ShipMethod.csv"
    employee_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/Employee.csv"
    poheader_csv = "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderHeader.csv"

    # Extract raw data
    SalesOrderDetail = pd.read_csv(salesorderdetail_csv, delimiter='\t')
    SalesTerritory = pd.read_csv(salesterritory_csv, delimiter='\t')
    PurchaseOrderDetail = pd.read_csv(purchaseorderdetail_csv, delimiter='\t')
    ShipMethod = pd.read_csv(shipmethod_csv, delimiter='\t')
    Employee = pd.read_csv(employee_csv, delimiter='\t', encoding='latin1')
    PurchaseOrderHeader = pd.read_csv(poheader_csv, delimiter='\t')

    # Debugging: Print column names before renaming
    print("Columns in SalesOrderDetail before renaming:", SalesOrderDetail.columns.tolist())

    # Apply transformations
    transformed_salesorderdetail = transform_salesorderdetail(SalesOrderDetail)
    transformed_purchaseorderdetail = transform_purchaseorderdetail(PurchaseOrderDetail)
    transformed_shipmethod = transform_shipmethod(ShipMethod)
    transformed_employee = transform_employee(Employee)
    transformed_purchaseorderheader = transform_purchaseorderheader(PurchaseOrderHeader)

    # Store transformed data
    transformed_salesorderdetail.to_csv("transformed_salesorderdetail.csv", index=False)
    transformed_purchaseorderdetail.to_csv("transformed_purchaseorderdetail.csv", index=False)
    transformed_shipmethod.to_csv("transformed_shipmethod.csv", index=False)
    transformed_employee.to_csv("transformed_employee.csv", index=False)
    transformed_purchaseorderheader.to_csv("transformed_purchaseorderheader.csv", index=False)

    print("All tables transformed successfully!")

if __name__ == "__main__":
    main()

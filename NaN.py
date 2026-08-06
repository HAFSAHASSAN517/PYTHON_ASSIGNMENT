import numpy as np
import pandas as pd
import re

def main():
    # --- Missing-value handling and interpolation ---
    data = {
        'Customer_ID': [101, 102, np.nan, 104, 105, 106, 107],
        'Age': [25, np.nan, 30, 22, 100, np.nan, 28],
        'Department': ['Sales', 'HR', 'IT', np.nan, 'HR', 'IT', 'Sales'],
        'Temperature_Sensor': [20.1, 20.4, np.nan, 21.2, 21.5, np.nan, 22.1]
    }
    df = pd.DataFrame(data)
    print("Nulls in initial dataframe:\n", df.isnull(), "\n")

    # drop rows without Customer_ID, then fill / interpolate
    df = df.dropna(subset=['Customer_ID']).copy()
    median_age = df['Age'].median()
    df['Age'] = df['Age'].fillna(median_age)
    df['Temperature_Sensor'] = df['Temperature_Sensor'].interpolate(method='linear')
    print("After filling/interpolating:\n", df, "\n")

    # --- Orders/Products merge and revenue calculation ---
    df_orders = pd.DataFrame({
        'Order_ID': [1001, 1002, 1003, 1004, 1005],
        'Product_ID': ['P01', 'P02', 'P01', 'P03', 'P02'],
        'Quantity_Sold': [2, 5, 1, 3, 4]
    })
    df_products = pd.DataFrame({
        'Product_ID': ['P01', 'P02', 'P03', 'P04'],
        'Product_Name': ['Wireless Mouse', 'Mechanical Keyboard', 'USB-C Cable', 'Monitor'],
        'Unit_Price': [25.00, 85.00, 12.50, 200.00],
        'Unit_Cost': [10.00, 45.00, 4.00, 110.00]
    })
    print("orders dataframe:")
    print(df_orders)
    print("products dataframe:")
    print(df_products)
    new_df = pd.merge(df_orders, df_products, on='Product_ID', how='left')
    print("merged dataframe:")
    print(new_df)
    total_revenue = (new_df['Quantity_Sold'] * new_df['Unit_Price']).sum()
    print(f"Total Revenue: ${total_revenue:.2f}\n")

    # --- Customer tier categorization ---
    df_customers = pd.DataFrame({
        'Customer_ID': [101, 102, 103, 104, 105],
        'Total_Spend': [1200, 450, 3200, 150, 800],
        'Account_Age_Days': [400, 150, 720, 30, 500],
        'Is_VIP_Member': [True, False, True, False, False]
    })
    print("customers dataframe:")

    def categorize_cus(row):
        spend = row['Total_Spend']
        age = row['Account_Age_Days']
        is_vip = row['Is_VIP_Member']
        if is_vip and spend > 2000:
            return 'Platinum'
        elif spend > 1000 or (age > 365 and is_vip):
            return 'Silver'
        else:
            return 'Bronze'

    df_customers['Customer_Tier'] = df_customers.apply(categorize_cus, axis=1)
    print(df_customers, "\n")

    # --- Sales pivot table by month/category ---
    sales_data = {
        'Transaction_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Date': pd.to_datetime([
            '2026-01-05', '2026-01-12', '2026-02-03', '2026-02-18', '2026-03-01',
            '2026-01-20', '2026-02-25', '2026-03-10', '2026-03-22', '2026-02-14'
        ]),
        'Category': [
            'Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics',
            'Furniture', 'Furniture', 'Clothing', 'Furniture', 'Electronics'
        ],
        'Revenue': [1500, 200, 800, 350, 1200, 600, 450, 500, 900, 1100]
    }
    df_sales = pd.DataFrame(sales_data)
    print(df_sales)
    df_sales['Month'] = df_sales['Date'].dt.strftime('%B')
    revenue = pd.pivot_table(
        data=df_sales,
        values='Revenue',
        index='Category',
        columns='Month',
        aggfunc='sum',
        fill_value=0,
        margins=True,
        margins_name='Total_revenue'
    )
    print("Revenue pivot:\n", revenue, "\n")

    # --- Raw data cleaning (column names, parsing dates) ---
    raw_data = {
        ' Customer ID ': [101, 102, 103, 104],
        'First Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'ORDER DATE': ['2026-01-15', '12/02/2026', '2026-03-01', '2026/03/20'],
        'Last Sign-In Date!': ['2026-05-01 10:30', '2026-05-02 11:45', '2026-05-03 09:15', '2026-05-04 14:00'],
        'Total Spent ($)': [150.50, 200.00, 310.25, 95.00]
    }
    df_raw = pd.DataFrame(raw_data)
    print("Raw dataframe columns before cleaning:", df_raw.columns.tolist())

    def clean_col(col_name):
        c = col_name.strip()
        c = re.sub(r"[^\w\s-]", "", c)
        c = re.sub(r"[\s-]+", "_", c)
        return c.lower()

    df_raw.columns = [clean_col(c) for c in df_raw.columns]
    print("Columns after cleaning:", df_raw.columns.tolist())

    # Parse mixed-format dates
    df_raw['order_date'] = pd.to_datetime(df_raw.get('order_date'), infer_datetime_format=True, dayfirst=False, errors='coerce')
    df_raw['last_sign_in_date'] = pd.to_datetime(df_raw.get('last_sign_in_date'), errors='coerce')
    print("Cleaned raw dataframe:\n", df_raw)


if __name__ == '__main__':
    main()
import pandas as pd
import sqlite3

# File paths
csv_files = {
    'customers': 'customers.csv',
    'products': 'products.csv',
    'orders': 'orders.csv',
    'order_items': 'order_items.csv',
    'payments': 'payments.csv'
}

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('ecommerce.db')

# Load each CSV into its corresponding table
for table_name, file_path in csv_files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Table '{table_name}' loaded successfully.")

# Close connection
conn.close()
print("All tables ingested into ecommerce.db.")

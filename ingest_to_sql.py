import sqlite3
import pandas as pd
import os

print("Starting SQL Ingestion Phase...")

# 1. Load the corporate CSV data using Pandas to read it cleanly
csv_path = "raw_corporate_data.csv"
if not os.path.exists(csv_path):
    print(f"❌ Error: {csv_path} not found in directory!")
    exit()

df = pd.read_csv(csv_path)

# Clean column names immediately (removes spaces/hyphens for clean SQL execution)
df.columns = df.columns.str.replace(' ', '_').str.replace('-', '_')

# 2. Spin up a local relational database file
db_name = "telecom.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# 3. Drop table if it exists to allow repeatable testing runs
cursor.execute("DROP TABLE IF EXISTS customer_churn;")

# 4. Convert the dataframe directly into a structured SQL table
df.to_sql("customer_churn", conn, index=False, if_exists="replace")

# 5. Verify the injection worked by counting records inside the database
cursor.execute("SELECT COUNT(*) FROM customer_churn;")
record_count = cursor.fetchone()[0]

print("--------------------------------------------------")
print(f"✅ Success! Local Database Engine Initialized: {db_name}")
print(f"🗂️ Table 'customer_churn' populated with {record_count} operational records.")
print("--------------------------------------------------")

conn.close()
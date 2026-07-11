import sqlite3
import pandas as pd

print("Extracting structured business features via SQL...")

# 1. Boot up connections
conn = sqlite3.connect("telecom.db")

# 2. Open and read your SQL script file
with open("extract_churn_features.sql", "r") as sql_file:
    query = sql_file.read()

# 3. Pull data straight out of the database into a Pandas Dataframe
df = pd.read_sql_query(query, conn)

# 4. Save to a staging file for our upcoming Power BI/Python work
df.to_csv("sql_extracted_churn_data.csv", index=False)

print("--------------------------------------------------")
print("✅ Success! SQL Script Executed Flawlessly.")
print("📂 File Created: sql_extracted_churn_data.csv")
print("--------------------------------------------------")

conn.close()
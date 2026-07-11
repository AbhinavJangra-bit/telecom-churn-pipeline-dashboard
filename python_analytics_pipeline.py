import pandas as pd
import numpy as np
import os

print("🚀 Launching Python Advanced Data Mining Phase...")

# 1. Load the dataset we extracted from SQL
source_file = "sql_extracted_churn_data.csv"
if not os.path.exists(source_file):
    print(f"❌ Error: {source_file} missing! Run execute_sql.py first.")
    exit()

df = pd.read_csv(source_file)

# 2. Data Cleaning: Strip any accidental spaces from text fields
string_cols = df.select_dtypes(include=['object']).columns
for col in string_cols:
    df[col] = df[col].str.strip()

# 3. Data Mining Rule 1: Calculate "Financial Velocity" (Monthly spend per month of tenure)
# To avoid division by zero for brand new users (tenure = 0), we use max(tenure, 1)
df['adjusted_tenure'] = df['tenure'].replace(0, 1)
df['spending_velocity'] = df['TotalCharges'] / df['adjusted_tenure']

# 4. Data Mining Rule 2: Outlier Detection for Monthly Spending using the IQR Method
# Let's find out what qualifies as an exceptionally high monthly bill in this company
q1 = df['MonthlyCharges'].quantile(0.25)
q3 = df['MonthlyCharges'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)

# Flag users who are paying outlier-level premium prices
df['is_premium_outlier'] = np.where(df['MonthlyCharges'] > upper_bound, 1, 0)

# 5. Data Mining Rule 3: Segment Churn Risk Zones using Conditional Logic
# High Risk = Month-to-Month contract AND has zero support protection features
# Medium Risk = Short tenure (less than 12 months) BUT has partial protection
# Low Risk = Long term contracts or fully protected
conditions = [
    (df['Contract'] == 'Month-to-month') & (df['protection_tier'] == 'No Support Features'),
    (df['tenure'] <= 12) & (df['protection_tier'] == 'Partially Protected'),
    (df['Contract'].isin(['One year', 'Two year'])) | (df['protection_tier'] == 'Fully Protected')
]
risk_labels = ['High Churn Risk', 'Medium Risk', 'Stable / Low Risk']

df['predicted_risk_segment'] = np.select(conditions, risk_labels, default='Review Needed')

# 6. Export the final, fully-enriched data asset for our Power BI Dashboard
output_file = "final_corporate_churn_analytics.csv"
df.drop(columns=['adjusted_tenure']).to_csv(output_file, index=False)

print("--------------------------------------------------")
print("✅ Success! Python Feature Engineering Complete.")
print(f"📊 Extracted premium bill cutoff: > ${upper_bound:.2f}/month")
print(f"📂 Output generated for Power BI: {output_file}")
print("--------------------------------------------------")
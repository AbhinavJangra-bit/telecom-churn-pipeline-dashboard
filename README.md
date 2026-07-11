# Telecom Customer Churn Data Pipeline & Executive Dashboard

An end-to-end data engineering and analytics pipeline that ingests raw customer log assets, structures relational data storage via SQL, executes statistical feature engineering with Python, and deploys an interactive executive business intelligence application.

## 🏢 Project Architecture & Data Flow
1. **Database Ingestion Layer (SQL/SQLite):** Securely ingests raw data assets, handles structural anomalies (safely forcing empty string billing artifacts to zero decimal values), and extracts initial business-focused columns.
2. **Advanced Feature Engineering (Python/Pandas/NumPy):** Automated calculation of *Financial Spending Velocity* and programmatic mapping of high-risk operational segments.
3. **Statistical Outlier Mining (IQR Method):** Implements an automated Interquartile Range (IQR) cutoff filter to isolate premium billing anomalies for special executive review.
4. **Business Intelligence Application (Power BI/DAX):** A seamless, interactive executive workspace displaying custom DAX business metrics like dynamic *Total Churn Count* and *Overall Churn Rate %*.

## 📂 Repository File Structure
* `/extract_churn_features.sql` - Production-grade query resolving data types and staging cohorts.
* `/execute_sql.py` - Automation engine connecting Python to the relational database framework.
* `/python_analytics_pipeline.py` - Core statistical data mining pipeline (IQR and conditional logic mapping).
* `/Churn_Executive_Dashboard.pbix` - Finished, production-ready interactive reporting application.

## 📊 Core Engineering Metric Implementation
* **Financial Velocity Formula:** 
  $$\text{Spending Velocity} = \frac{\text{Total Charges}}{\text{Max}(\text{Tenure}, 1)}$$
* **Predictive Segmentation Logic:** High Risk flags are assigned to short-term, month-to-month contracts completely lacking protective customer technical support features.
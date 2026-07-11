import os
import urllib.request

def fetch_corporate_data():
    # 1. Setup paths
    target_filename = "raw_corporate_data.csv"
    
    # Official IBM dataset host link
    source_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    
    print(f"Connecting to corporate repository to pull churn logs...")
    
    try:
        # 2. Stream and download the data file directly into our workspace
        urllib.request.urlretrieve(source_url, target_filename)
        
        if os.path.exists(target_filename):
            file_size_kb = os.path.getsize(target_filename) / 1024
            print("--------------------------------------------------")
            print(f"✅ Success! Raw data asset generated: {target_filename}")
            print(f"📂 File Size: {file_size_kb:.2f} KB")
            print("--------------------------------------------------")
        else:
            print("❌ Download finished but file could not be verified.")
            
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")

if __name__ == "__main__":
    fetch_corporate_data()
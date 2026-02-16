import pandas as pd
from ydata_profiling import ProfileReport
import os

def main():
    csv_file = 'Dataset.csv'
    xlsx_file = 'Dataset.xlsx'

    # Check if CSV exists
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    print(f"Loading {csv_file}...")
    try:
        df = pd.read_csv(csv_file)
        print("Dataset loaded successfully.")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # --- Preprocessing (optional, same as before) ---
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        print("Converted 'Timestamp' to datetime.")

    # --- EDA Report ---
    print("Generating EDA report...")
    try:
        profile = ProfileReport(df, title="EDA Profiling Report", explorative=True)
        profile.to_file("eda_report.html")
        print("EDA report saved to 'eda_report.html'.")
    except Exception as e:
        print(f"Error generating EDA report: {e}")

    # --- CSV to XLSX Conversion ---
    print(f"Converting {csv_file} to {xlsx_file}...")
    try:
        # Requires openpyxl
        df.to_excel(xlsx_file, index=False, engine='openpyxl')
        print(f"Successfully created {xlsx_file}.")
    except ImportError:
        print("Error: 'openpyxl' library is missing. Please run: pip install openpyxl")
    except Exception as e:
        print(f"Error converting to Excel: {e}")

if __name__ == "__main__":
    main()

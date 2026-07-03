import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

def generate_mock_dataset():
    """Scrapes titles or uses fallback values, then builds a NumPy/Pandas dataset."""
    print("Initializing dataset generation...")
    try:
        response = requests.get("https://toscrape.com", timeout=5)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        book_pods = soup.find_all("article", class_="product_pod")
        titles = [pod.h3.a["title"] for pod in book_pods]
    except Exception:
        titles = []

    # Safety fallback if scraping returns zero items
    if not titles:
        titles = [f"Product Asset {i}" for i in range(1, 21)]

    # Matrix configuration
    np.random.seed(42)
    rows = 50
    
    # Repeat/slice items to fit target dimensions
    base_items = (titles * ((rows // len(titles)) + 1))[:rows]
    
    # Structural matrices
    regions = ["North", "South", "East", "West", "Central"]
    teams = ["MI", "CSK", "RCB", "KKR", "SRH", "DC", "RR", "LSG"]
    
    # Generate synthetic numeric metrics using NumPy distributions
    units_sold = np.random.randint(10, 500, size=rows)
    gross_revenue = np.random.uniform(500.0, 15000.0, size=rows).round(2)
    match_attendance = np.random.normal(35000, 8000, size=rows).astype(int)
    
    # Randomly assign categorical elements
    assigned_regions = np.random.choice(regions, size=rows)
    assigned_teams = np.random.choice(teams, size=rows)
    
    # Combine into a Pandas DataFrame
    df = pd.DataFrame({
        "Product_Title": base_items,
        "Region": assigned_regions,
        "Associated_Team": assigned_teams,
        "Units_Sold": units_sold,
        "Gross_Revenue": gross_revenue,
        "Match_Attendance": match_attendance
    })
    
    df.to_csv("ipl_sales_records.csv", index=False)
    print("✔ Dataset generated successfully and saved to 'ipl_sales_records.csv'.\n")
    return df

def display_statistics_dashboard(df):
    """Computes descriptive statistics using NumPy/Pandas and displays a CLI report."""
    print("=" * 60)
    print("         NUMPY STATISTICS DASHBOARD (CLI SUMMARY)         ")
    print("=" * 60)
    
    # Extract underlying raw NumPy arrays from the DataFrame columns
    units_arr = df["Units_Sold"].to_numpy()
    revenue_arr = df["Gross_Revenue"].to_numpy()
    attendance_arr = df["Match_Attendance"].to_numpy()
    
    metrics = {
        "Units Sold": units_arr,
        "Gross Revenue (£)": revenue_arr,
        "Match Attendance": attendance_arr
    }
    
    # Compute descriptive metrics using core NumPy functions
    for name, array in metrics.items():
        print(f"\n📊 Metrics Overview: {name}")
        print(f"  • Count (n)     : {len(array)}")
        print(f"  • Mean          : {np.mean(array):,.2f}")
        print(f"  • Median        : {np.median(array):,.2f}")
        print(f"  • Std Deviation : {np.std(array):,.2f}")
        print(f"  • Minimum       : {np.min(array):,}")
        print(f"  • Maximum       : {np.max(array):,}")
        print(f"  • Range         : {(np.max(array) - np.min(array)):,}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    # Generate data and build the command-line dashboard
    sales_df = generate_mock_dataset()
    display_statistics_dashboard(sales_df)
import pandas as pd
import matplotlib.pyplot as plt
import os

def analyze_data():
    os.makedirs("Analysis", exist_ok=True)
    csv_file = "Mutual_Fund_Datas/mutual_fund_analysis.csv"

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print("Error reading CSV:", e)
        return

    print("Initial Data Overview:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    df_cleaning = df.dropna(subset=["NAV", "1y Return (%)", "3y Return (%)"]).copy()

    try:
        df_cleaning["1y Return (%)"] = (df_cleaning["1y Return (%)"].astype(str).str.replace("%", "", regex=False).str.replace("+", "", regex=False).str.replace(",", "", regex=False).astype(float))
        df_cleaning["3y Return (%)"] = (df_cleaning["3y Return (%)"].astype(str).str.replace("%", "", regex=False).str.replace("+", "", regex=False).str.replace(",", "", regex=False).astype(float))
        df_cleaning["NAV"] = (df_cleaning["NAV"].astype(str).str.replace("₹", "", regex=False).str.replace(",", "", regex=False).astype(float))

    except Exception as e:
        print("Data Conversion Error:", e)
        return

    print("\nData Types:")
    print(df_cleaning.dtypes)

    cleaned_file = "Mutual_Fund_Datas/mutual_funds_cleaning.csv"
    df_cleaning.to_csv(cleaned_file, index=False)
    print(f"\nCleaned CSV Saved: {cleaned_file}")

    df_sorted = df_cleaning.sort_values(by="1y Return (%)", ascending=False)
    top_10_funds = df_sorted.head(10)
    
    plt.figure(figsize=(15, 8))
    plt.barh(top_10_funds["Mutual Fund Name"], top_10_funds["1y Return (%)"])
    plt.title("Top 10 Mutual Funds by 1-Year Return")
    plt.xlabel("1-Year Return (%)")
    plt.ylabel("Mutual Fund Name")
    plt.tight_layout()
    plt.savefig("Analysis/top_10_funds_1y_return.png")
    plt.show()

    plt.figure(figsize=(15, 8))
    plt.bar(top_10_funds["Mutual Fund Name"], top_10_funds["3y Return (%)"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Top 10 Mutual Funds by 3-Year Return")
    plt.xlabel("Mutual Fund Name")
    plt.ylabel("3-Year Return (%)")
    plt.tight_layout()
    plt.savefig("Analysis/top_10_funds_3y_return.png")
    plt.show()

    plt.figure(figsize=(15, 8))
    width = 0.35
    x = range(len(top_10_funds))
    plt.bar([i - width / 2 for i in x], top_10_funds["1y Return (%)"], width, label="1-Year")
    plt.bar([i + width / 2 for i in x], top_10_funds["3y Return (%)"], width, label="3-Year")
    plt.xticks(x,top_10_funds["Mutual Fund Name"], rotation=45, ha="right")
    plt.title("1-Year vs 3-Year Return")
    plt.xlabel("Mutual Fund Name")
    plt.ylabel("Return (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Analysis/top_10_funds_1y_vs_3y_return.png")
    plt.show()

    category_group = (df_cleaning.groupby("Category")[["1y Return (%)", "3y Return (%)"]].mean().round(2))
    print("\nAverage Return By Category")
    print(category_group)

    category_group.to_csv("Analysis/category_analysis.csv")
    risk_group_1y = (df_cleaning.groupby("Risk Level")["1y Return (%)"].mean())

    plt.figure(figsize=(10, 6))
    risk_group_1y.plot(kind="bar")
    plt.title("Average 1-Year Return by Risk Level")
    plt.xlabel("Risk Level")
    plt.ylabel("Average Return (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("Analysis/avg_1y_risk_return.png")
    plt.show()

    risk_group_3y = (df_cleaning.groupby("Risk Level")["3y Return (%)"].mean())
    plt.figure(figsize=(10, 6))
    risk_group_3y.plot(kind="bar")
    plt.title("Average 3-Year Return by Risk Level")
    plt.xlabel("Risk Level")
    plt.ylabel("Average Return (%)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("Analysis/avg_3y_risk_return.png")
    plt.show()

    print("\nCorrelation Matrix")
    correlation = (df_cleaning[["NAV", "1y Return (%)", "3y Return (%)"]].corr().round(2))
    
    print(correlation)
    correlation.to_csv("Analysis/correlation_matrix.csv")
    best_1y = df_cleaning.loc[df_cleaning["1y Return (%)"].idxmax()]
    
    print("\nBest Fund (1-Year Return)")
    print(best_1y)

    best_3y = df_cleaning.loc[df_cleaning["3y Return (%)"].idxmax()]
    print("\nBest Fund (3-Year Return)")
    print(best_3y)
    print("\nAnalysis Completed Successfully")

if __name__ == "__main__":
    analyze_data()
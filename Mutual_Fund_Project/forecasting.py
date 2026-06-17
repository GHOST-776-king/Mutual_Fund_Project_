import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import os


def forecast_file():
    os.makedirs("Forecasting_graph", exist_ok=True)
    csv_file = "Mutual_Fund_Datas/mutual_funds_cleaning.csv"

    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print("CSV Read Error:", e)
        return

    print("Loaded Cleaned Data:")
    print(df.head())

    try:
        best_fund = df.loc[df["1y Return (%)"].idxmax()]
    except Exception as e:
        print("Fund Selection Error:", e)
        return

    fund_name = best_fund["Mutual Fund Name"]
    start_nav = float(best_fund["NAV"])
    print("\nSelected Fund For Forecasting")
    print("Fund Name :", fund_name)
    print("Current NAV :", start_nav)

    def generate_nav(start_nav, days=365):
        dates = [datetime.now() - timedelta(days=i) for i in range(days)]
        dates.reverse()
        navs = [start_nav]

        for _ in range(1, days):
            change = np.random.normal(loc=0.02, scale=0.5)
            new_nav = max(10, navs[-1] + change)
            navs.append(new_nav)
            
        return pd.DataFrame({
            "Date": dates,
            "NAV": navs
        })
    df_hist = generate_nav(start_nav)
    df_hist.to_csv("Mutual_Fund_Datas/historical_nav.csv", index=False)
    print("\nHistorical Data Saved")

    df_hist["SMA_30"] = (df_hist["NAV"].rolling(window=30).mean())
    df_hist["SMA_90"] = (df_hist["NAV"].rolling(window=90).mean())

    plt.figure(figsize=(14, 7))
    plt.plot(df_hist["Date"], df_hist["NAV"], label="Daily NAV")
    plt.plot(df_hist["Date"], df_hist["SMA_30"], label="30-Day SMA")
    plt.plot(df_hist["Date"],df_hist["SMA_90"], label="90-Day SMA")
    plt.title(f"{fund_name}\nMoving Averages")
    plt.xlabel("Date")
    plt.ylabel("NAV")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Forecasting_graph/moving_averages.png")
    plt.show()

    df_hist["Days"] = (df_hist["Date"] - df_hist["Date"].min()).dt.days
    X = df_hist[["Days"]]
    y = df_hist["NAV"]
    model = LinearRegression()
    model.fit(X, y)
    score = model.score(X, y)

    print(f"\nIntercept : {model.intercept_:.2f}")
    print(f"Slope : {model.coef_[0]:.4f}")
    print(f"R² Score : {score:.4f}")

    future_days_count = 30
    last_day = df_hist["Days"].max()
    future_days = pd.DataFrame({"Days": [last_day + i for i in range(1, future_days_count + 1)]})
    future_predictions = model.predict(future_days)
    last_date = df_hist["Date"].max()
    future_dates = [last_date + timedelta(days=i) for i in range(1, future_days_count + 1)]

    plt.figure(figsize=(14, 7))
    plt.plot(df_hist["Date"], df_hist["NAV"], label="Historical NAV")
    plt.plot(df_hist["Date"], model.predict(X), linestyle="--", label="Regression Trend")
    plt.plot(future_dates, future_predictions, linewidth=3, label="30-Day Forecast")
    plt.title(f"{fund_name}\nFuture NAV Forecast")
    plt.xlabel("Date")
    plt.ylabel("NAV")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Forecasting_graph/nav_forecast.png")
    plt.show()

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Predicted NAV": future_predictions
        })
    forecast_df.to_csv("Mutual_Fund_Datas/forecast_30_days.csv", index=False)

    print("\nForecast CSV Saved Successfully")
    print(forecast_df.head())

    with open("Reports/forecast_report.txt", "w", encoding="utf-8") as f:
        f.write("MUTUAL FUND FORECAST REPORT\n")
        f.write("=" * 100 + "\n\n")
        f.write(f"Fund Name : {fund_name}\n")
        f.write(f"Current NAV : {start_nav:.2f}\n")
        f.write(f"Predicted NAV After 30 Days : "f"{future_predictions[-1]:.2f}\n")
        f.write(f"Regression R² Score : "f"{score:.4f}\n")

    print("Forecast Report Saved Successfully")
    print("\nForecasting Completed Successfully")

if __name__ == "__main__":
    forecast_file()
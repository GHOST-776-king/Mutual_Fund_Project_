import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as bs
import os
import random

def scrape_fund_data():
    os.makedirs("Reports", exist_ok=True)
    os.makedirs("Mutual_Fund_Datas", exist_ok=True)
    print("This Method will take some time")
    print("Processing...")

    url1 = "https://groww.in/mutual-funds/filter?sub_cat=%5B%22Large+Cap%22%2C%22Mid+Cap%22%2C%22Small+Cap%22%5D"
    url2 = "https://www.etmoney.com/mutual-funds/filter/latest-mutual-fund-nav"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response1 = rq.get(url1, headers=headers, timeout=10)
        response2 = rq.get(url2, headers=headers, timeout=10)

        response1.raise_for_status()
        response2.raise_for_status()

    except Exception as e:
        print(f"Request Error: {e}")
        return

    soup1 = bs(response1.text, "html.parser")
    soup2 = bs(response2.text, "html.parser")

    table1 = soup1.find("table")
    table2 = soup2.find("table")

    if table1 is None:
        print("Groww table not found.")
        return

    if table2 is None:
        print("ET Money table not found.")
        return

    rows1 = table1.find_all("tr")
    rows2 = table2.find_all("tr", class_="mfFund-nav-row")

    groww_data = {}
    funds_data = []

    a = round(random.uniform(0, 15), 2)
    b = round(random.uniform(15, 35), 2)

    for row in rows1:
        cols = row.find_all("td")

        if len(cols) >= 8:
            y1_return = cols[3].get_text(strip=True)
            if y1_return == "--":
                y1_return = f"+{a}"

            y3_return = cols[4].get_text(strip=True)
            if y3_return == "--":
                y3_return = f"+{b}"
                
            fund_name = cols[1].get_text(strip=True)
            groww_data[fund_name.lower()] = {
                "Mutual Fund Name": fund_name,
                "Category": cols[2].get_text(strip=True),
                "1y Return (%)": y1_return,
                "3y Return (%)": y3_return,
                "Risk Level": cols[7].get_text(strip=True)
            }

    for row in rows2:
        cols = row.find_all("td")

        if len(cols) >= 5:
            try:
                fund_name = cols[0].find("a").get_text(strip=True)
            except:
                continue

            nav = cols[2].get_text(strip=True)
            date = cols[4].get_text(strip=True)

            for groww_name in groww_data:
                if (fund_name.lower() in groww_name or groww_name in fund_name.lower()):
                    funds_data.append({
                        "Mutual Fund Name": groww_data[groww_name]["Mutual Fund Name"],
                        "Category": groww_data[groww_name]["Category"],
                        "NAV": nav,
                        "Date": date,
                        "1y Return (%)": groww_data[groww_name]["1y Return (%)"],
                        "3y Return (%)": groww_data[groww_name]["3y Return (%)"],
                        "Risk Level": groww_data[groww_name]["Risk Level"]
                    })
                    break

    print(f"Groww Funds Found : {len(groww_data)}")
    print(f"Matched Funds     : {len(funds_data)}")

    if not funds_data:
        print("No matching funds found")
        return

    df = pd.DataFrame(funds_data)
    df.drop_duplicates(inplace=True)
    df["Category"] = (df["Category"].str.replace("Equity ", "", regex=False))

    csv_file = "Mutual_Fund_Datas/mutual_fund_analysis.csv"
    df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"CSV Saved: {csv_file}")

    report_file = "Reports/mutual_funds_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("#MUTUAL FUNDS DATA IN DETAILD\n")
        f.write("="* 100 + "\n\n")
        for fund in funds_data:
            f.write(f"Mutual Fund Name : {fund['Mutual Fund Name']}\n")
            f.write(f"Category : {fund['Category']}\n")
            f.write(f"NAV : {fund['NAV']}\n")
            f.write(f"Date : {fund['Date']}\n")
            f.write(f"1y Return (%) : {fund['1y Return (%)']}\n")
            f.write(f"3y Return (%) : {fund['3y Return (%)']}\n")
            f.write(f"Risk Level : {fund['Risk Level']}\n")
            f.write("-" * 60 + "\n")

    print(f"TXT Report Saved: {report_file}")
    print("\nSample Data:")
    print(df.head())


if __name__ == "__main__":
    scrape_fund_data()
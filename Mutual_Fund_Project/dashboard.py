import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Mutual Fund Trend Analyzer", layout="wide")
st.title("Mutual Fund Trend Analyzer")
st.markdown("Mutual Fund Data Scraper & Forecasting System")

csv_file = "Mutual_Fund_Datas/mutual_fund_analysis.csv"
clean_file = "Mutual_Fund_Datas/mutual_funds_cleaning.csv"
forecast_file = "Mutual_Fund_Datas/forecast_30_days.csv"

if not os.path.exists(csv_file):
    st.error("mutual_fund_analysis.csv not found")
    st.stop()

df = pd.read_csv(csv_file)
st.sidebar.title("Navigation")

page = st.sidebar.radio("Select Page", ["Dashboard", "Fund Data", "Top Funds", "Analysis Graphs", "Forecast"])

if page == "Dashboard":
    st.subheader("Project Overview")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Funds", len(df))

    with col2:
        st.metric("Categories", df["Category"].nunique())

    with col3:
        st.metric("Risk Levels", df["Risk Level"].nunique())
    st.markdown("---")
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "Fund Data":
    st.subheader("Mutual Fund Dataset")
    search = st.text_input("Search Fund")

    if search:
        filtered = df[df["Mutual Fund Name"].str.contains(search, case=False, na=False)]
        st.dataframe(filtered, use_container_width=True)

    else:
        st.dataframe(df, use_container_width=True)

elif page == "Top Funds":
    st.subheader("Top Performing Funds")

    if os.path.exists(clean_file):
        clean_df = pd.read_csv(clean_file)
        top_funds = clean_df.sort_values(by="1y Return (%)", ascending=False).head(10)
        st.dataframe(top_funds, use_container_width=True)

    else:
        st.warning("Run analysis.py first")

elif page == "Analysis Graphs":
    st.subheader("Analysis Graphs")

    graph_files = [
        "Analysis/top_10_funds_1y_return.png",
        "Analysis/top_10_funds_3y_return.png",
        "Analysis/top_10_funds_1y_vs_3y_return.png",
        "Analysis/avg_1y_risk_return.png",
        "Analysis/avg_3y_risk_return.png"
        ]

    for graph in graph_files:
        if os.path.exists(graph):
            st.image(graph, use_container_width=True)
            
        else:
            st.warning(f"{graph} not found")

elif page == "Forecast":
    st.subheader("Forecasting Results")
    graph = ("Forecasting_graph/" "nav_forecast.png")

    if os.path.exists(graph):
        st.image(graph, use_container_width=True)

    else:
        st.warning("Run forecasting.py first")

    if os.path.exists(forecast_file):
        forecast_df = pd.read_csv(forecast_file)
        st.subheader("Next 30 Days Prediction")
        st.dataframe(forecast_df, use_container_width=True)

    else:
        st.warning("forecast_30_days.csv not found")

st.sidebar.markdown("---")
st.sidebar.success("Mutual Fund Trend Analyzer")
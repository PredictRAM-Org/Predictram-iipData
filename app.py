import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Function to load stock data from the "Stock_Data" folder
def load_stock_data():
    stock_data = {}
    folder_path = "Stock_Data"

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xlsx"):
            stock_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(folder_path, file_name)
            stock_data[stock_name] = pd.read_excel(file_path)

    return stock_data

# Function to plot separate and combined graphs
def plot_graphs(stock_data, selected_stock):
    # Check if 'Industry' is present in the stock data
    if 'Industry' not in stock_data:
        st.error("Error: 'Industry' stock data not found.")
        return

    # Check if the selected stock is present in the stock data
    if selected_stock not in stock_data:
        st.error(f"Error: Stock data for {selected_stock} not found.")
        return

    # Plot separate graph for industry
    fig_industry = px.line(stock_data['Industry'], x="Date", y="Close", title="Industry Close Price")
    st.plotly_chart(fig_industry)

    # Plot separate graph for the selected stock
    fig_selected_stock = px.line(stock_data[selected_stock], x="Date", y="Close", title=f"{selected_stock} Close Price")
    st.plotly_chart(fig_selected_stock)

    # Plot combined graph for industry and selected stock
    fig_combined = px.line(stock_data[selected_stock], x="Date", y="Close", title=f"Industry and {selected_stock} Close Price")
    fig_combined.add_trace(px.line(stock_data['Industry'], x="Date", y="Close", line_dash="dash", name="Industry").data[0])
    st.plotly_chart(fig_combined)

# Load stock data
stock_data = load_stock_data()

# Streamlit app
st.title("Stock Data Visualization App")

# Sidebar
st.sidebar.header("Select Options")

# Check if 'Industry' is present before displaying the option
if 'Industry' in stock_data:
    selected_stock = st.sidebar.selectbox("Select Stock", ['Industry'] + list(stock_data.keys()), index=1)
    # Plot graphs
    plot_graphs(stock_data, selected_stock)
else:
    st.sidebar.warning("Warning: 'Industry' stock data not found.")

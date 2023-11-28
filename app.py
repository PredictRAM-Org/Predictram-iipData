import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from the Excel file
file_path = "IIP_Data.xlsx"
df = pd.read_excel(file_path)

# Convert "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors='coerce')

# Streamlit app
st.title("IIP Data Visualization App")

# Sidebar
st.sidebar.header("Select Options")
selected_column = st.sidebar.selectbox("Select Column", df.columns[1:])

# Default start date
default_start_date = pd.to_datetime("2012-04-01")

# Date input widget with default value
start_date = st.sidebar.date_input("Select Start Date", default_start_date)

# Ensure that the start_date is a Timestamp object
start_date = pd.to_datetime(start_date)

# Filter data based on user selection
filtered_df = df[df["Date"] >= start_date]

# Plot the selected column
fig = px.line(filtered_df, x="Date", y=selected_column, title=f"{selected_column} over Time")
st.plotly_chart(fig)

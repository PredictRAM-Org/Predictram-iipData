import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from the Excel file
file_path = "IIP_Data.xlsx"
df = pd.read_excel(file_path)

# Convert "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%Y:%m", errors='coerce')

# Streamlit app
st.title("IIP Data Visualization App")

# Sidebar
st.sidebar.header("Select Options")
selected_column = st.sidebar.selectbox("Select Column", df.columns[1:])

# Convert the minimum date to a string in the required format
start_date_str = df["Date"].min().strftime("%Y:%m")
start_date = st.sidebar.date_input("Select Start Date", pd.to_datetime(start_date_str))

# Filter data based on user selection
filtered_df = df[df["Date"] >= start_date]

# Plot the selected column
fig = px.line(filtered_df, x="Date", y=selected_column, title=f"{selected_column} over Time")
st.plotly_chart(fig)

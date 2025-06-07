
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sales Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Preview:", df.head())

    # Sidebar filter
    gender_filter = st.sidebar.selectbox("Select Gender", options=df["Gender"].unique())
    filtered_df = df[df["Gender"] == gender_filter]

    # Bar chart of sales by region
    chart_data = filtered_df.groupby("Region")["Sales"].sum().reset_index()
    st.bar_chart(chart_data.set_index("Region"))

    # Pie chart of Target counts
    pie_data = filtered_df["Target"].value_counts()
    st.write("### Target Distribution")
    st.pyplot(pie_data.plot.pie(autopct='%1.1f%%', figsize=(5, 5)).get_figure())

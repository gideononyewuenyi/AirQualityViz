"""
Plot air quality over time.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# TODO: Add a title for the web app
st.title("Air quality viz")

# TODO: Add a short text description what the web app does
st.subheader("Chart showing PM2.5 for june 1st, 2021 in Lagos, Nigeria")

# Load data is done for you
url = "https://raw.githubusercontent.com/gideononyewuenyi/Exploratory-analysis/main/Lekki%20Phase%201%20(outside)%20(6.451397%203.471201)%20Primary%2030_minute_average%2012_17_2019%206_6_2021.csv"
df = pd.read_csv(url)
# TODO: Create sliders for start index and number of months


# Select just the rows and single column to plot
data = df.iloc[37101:37150]
data = data[['PM2.5_ATM_ug/m3', 'Temperature_F', 'Humidity_%']]
plt.plot(data, subplots=True, x = 'Date/Time', figsize=(14,8))

# TODO: Create a line chart of the data
st.line_chart(data)

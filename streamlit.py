import streamlit as st 
import pandas as pd
import altair as alt
#import plotly.express as px
import numpy as np
import math
import random
alt.themes.enable("dark")
#used to add the title of an app
st.title("Study of Weather Data of Bangalore using Exploratory Data Analysis")
#header 
st.markdown("## Objective:")
#writing
st.markdown("##### To analyse the weather change based  on the weather data set")

st.markdown("## Overview:")
st.write("This project aims to identify patterns, trends, and anomalies in weather conditions over a specified period. By leveraging statistical analysis and data visualization techniques, we hope to gain a deeper understanding of how climate factors have evolved and how they might continue to change in the future. The insights derived from this analysis will be crucial for informing environmental policies, enhancing preparedness for extreme weather events, and fostering sustainable practices. Ultimately, the goal is to contribute to a broader understanding of climate dynamics and support efforts to mitigate the impact of climate change on our communities and ecosystems.")

st.markdown("## Why are we doing the Analysis on Bangalore only Given that we can choose any Region ?")
st.write("We’re analyzing Bangalore’s climate change because it’s a rapidly growing city that has undergone massive urbanization, which impacts its weather patterns. Bangalore's rainfall is highly dependent on monsoons, but climate change has led to irregular rainfall patterns Heavy rains or droughts occur unexpectedly, often outside the typical monsoon season. As a major tech and economic hub, changes in temperature and rainfall can affect millions of people and industries. Bangalore relies heavily on seasonal rains, so shifts in these patterns could lead to water shortages. Studying Bangalore helps us understand how urbanization affects climate, provides insights for better city planning, and contributes to global knowledge on climate change. It can also guide other cities facing similar challenges to adapt better<with distinct wet and dry seasons influenced by the southwest and northeast monsoons. However, in recent years, it has become less predictable due to the effects of climate change and urbanization.")

# Read the CSV file
data = pd.read_csv("bangalore.csv")
#dataset preview
st.write("## Dataset Preview:")
st.write("Here's a quick look at the first 5 rows of the dataset:")
st.dataframe(data.head()) # Display the first 5 rows of the dataset

#basic  statistics
st.write("## Basic Statistics:")
st.write("Provides statistical summaries (e.g., mean, min, max) for numerical columns.")
st.write(data.describe())

# Plotting the data
st.write("## Data Visualization")
st.write(" Here's a Customizable Line chart whwere you can visualize the data by selecting one or multiple columns to analyze trends.")
#x_column = "time"  # Replace with the desired X-axis column name
#y_columns = ["tavg", "prcp"]  # Replace with the desired Y-axis column names

# Ensure the columns exist in the dataset
#if x_column in data.columns and all(col in data.columns for col in y_columns):
# Plot the chart using Plotly
    #fig = px.line(data, x=x_column, y=y_columns, title="Line Chart Showing Average Temperature & Precipitation over the Years")
    #st.plotly_chart(fig)
#else:
    #st.error("Specified columns are not found in the dataset.")
if len(data) >= 20:
    chart_data = data.head(20)  # Get the first 20 rows
else:
    chart_data = data  # If less than 20 rows, use the whole dataset

# Allow users to choose columns to visualize
y_columns = st.multiselect("Select columns to plot on the Y-axis", data.columns.difference(['time']))

# Plot the line chart
if y_columns:
    st.line_chart(data.set_index('time')[y_columns])
else:
    st.write("Please select at least one column to display the line chart.")


#our demo video heading
st.markdown("## Demo Video")
#out demo video
st.video("https://youtu.be/1apHg99cyc4?si=IpDRQcdoayCm-3-0")

st.markdown("## Presentation")
st.write("Contains all the details about the project and  more data visualizations")
# Button that links to the ppt document
if st.button("View Presentation"):
    st.write("[Open Document](https://www.canva.com/design/DAGW1oz6WQo/IONhwBGbkWBi8rfPj_eVrQ/view?utm_content=DAGW1oz6WQo&utm_campaign=designshare&utm_medium=link&utm_source=editor )")


#button that links to the project report
st.markdown("## Project Report")
st.write("For More Insights here is the documentation")
if st.button("View Report"):
    st.write("[Open Document](https://docs.google.com/document/d/1sF6V4zNP9xM5I0OCnjZJkvNwnd7v1EZY/edit?usp=sharing&ouid=106051408725906265648&rtpof=true&sd=true)")

#conclusion heading
st.markdown("## Conclusion:")

#conclusion content
st.write("###### Based on the collective set of graphs and analysis provided:")
st.write("1)Temperature patterns are relatively stable and predictable over time, showing consistent seasonal cycles.")
st.write("2)Past temperature data can reliably forecast future temperatures.")
st.write("3)Precipitation patterns are much more irregular and variable, with high uncertainty in forecasting rainfall beyond the immediate timeframe.")
st.write("4)Past rainfall is not a strong predictor of future precipitation.")
st.write("5)The temperature distribution histogram indicates most days fall within a moderate temperature range around 24°C, with fewer instances of extremely hot or cold temperatures.")
st.write("6)The autocorrelation analysis further confirms the contrast - temperature has a strong, persistent relationship over time, while precipitation exhibits a weaker relationship beyond the short-term.")
st.write("###### In summary, the data suggests that while temperature follows a predictable cyclical pattern, precipitation has become increasingly unpredictable and less correlated with past weather trends. This points to a climate system where temperature variability is relatively stable, but rainfall patterns are becoming more erratic and difficult to forecast accurately.")

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Optional: Improve plot aesthetics
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load the dataset directly from URL or local CSV file
# (Our World in Data URL used as an example)
data_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(data_url, parse_dates=["date"])

# Quick look at the data
print(df.head())
print(df.info())

# Remove duplicate rows (if any)
df = df.drop_duplicates()

# For the purpose of the analysis, remove rows missing key metrics (e.g., total cases or total deaths)
df = df.dropna(subset=["total_cases", "total_deaths"])

# Convert the location column to a categorical type for faster operations
df["location"] = df["location"].astype("category")

# Inspect the cleaned data
print(df.describe())

# Let's analyze daily new cases for the United States
usa_data = df[df["location"] == "United States"]

# Plot using Seaborn
plt.figure(figsize=(14, 7))
sns.lineplot(x="date", y="new_cases", data=usa_data)
plt.title("Daily New COVID-19 Cases in the United States")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.show()

# Global daily new cases over time
global_trends = df.groupby("date")["new_cases"].sum().reset_index()

plt.figure(figsize=(14, 7))
sns.lineplot(x="date", y="new_cases", data=global_trends)
plt.title("Global Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.show()

# Select numeric columns of interest for a correlation matrix
selected_vars = ["total_cases", "total_deaths", "total_vaccinations", "new_cases", "new_deaths"]
corr_data = df[selected_vars].dropna()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix for COVID-19 Metrics")
plt.show()

# Interactive Plotly line chart – Daily New Cases for a Country
fig = px.line(usa_data, x="date", y="new_cases", 
              title="Interactive Chart: Daily New Cases in the United States",
              labels={"new_cases": "New Cases", "date": "Date"})
fig.show()

# Save this as app.py to run with the command 'streamlit run app.py'
import streamlit as st

st.set_page_config(layout="wide")
st.title("Global COVID-19 Trends Dashboard")

# Load data with caching for efficiency
@st.cache
def load_data():
    df = pd.read_csv(data_url, parse_dates=["date"])
    df = df.drop_duplicates().dropna(subset=["total_cases", "total_deaths"])
    df["location"] = df["location"].astype("category")
    return df

df = load_data()

# Add a multiselect widget for countries
countries = st.multiselect("Select Countries", options=df["location"].unique(), default=["United States", "India", "Brazil"])

# Filter data by selected countries
filtered_data = df[df["location"].isin(countries)]

# Display an interactive line chart of new cases
st.subheader("Daily New Cases")
pivot_df = filtered_data.pivot_table(index="date", columns="location", values="new_cases", aggfunc="sum")
st.line_chart(pivot_df)

# Additional widgets or charts can be added similarly

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Set up the page layout
st.set_page_config(page_title="My Health Dashboard", page_icon="🏃")
st.title("🏃 My Personal Health Insights")
st.markdown("Welcome to your vibe-coded app! This is currently using mock data to test the layout.")
st.divider()

# 2. Generate Fake Data (To simulate Google Health)
@st.cache_data
def generate_mock_data():
    today = datetime.today().date()
    # Create a list of the last 365 days
    dates = [today - timedelta(days=i) for i in range(365)]
    # Generate random steps between 4,000 and 15,000 for each day
    steps = np.random.randint(4000, 15000, size=365)
    
    df = pd.DataFrame({'Date': dates, 'Steps': steps})
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    return df

data = generate_mock_data()

# 3. Calculate the YTD, MTD, and WTD logic
today = datetime.today().date()

# YTD
start_of_year = today.replace(month=1, day=1)
ytd_steps = int(data[data['Date'] >= start_of_year]['Steps'].sum())

# MTD
start_of_month = today.replace(day=1)
mtd_steps = int(data[data['Date'] >= start_of_month]['Steps'].sum())

# WTD (Assuming Monday is the start of the week)
start_of_week = today - timedelta(days=today.weekday())
wtd_steps = int(data[data['Date'] >= start_of_week]['Steps'].sum())

# 4. Build the Visuals!
# Create 3 columns for our metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Steps (YTD)", value=f"{ytd_steps:,}")
with col2:
    st.metric(label="Total Steps (MTD)", value=f"{mtd_steps:,}")
with col3:
    st.metric(label="Total Steps (WTD)", value=f"{wtd_steps:,}")

# Add a chart for the last 30 days
st.subheader("Your Last 30 Days")
last_30_days = data.head(30).set_index('Date')
st.bar_chart(last_30_days['Steps'])

# Add the insight container
st.info("💡 **Smart Insight:** Your Week-to-Date average is looking strong! Once we connect real Google Health data, this box will compare your current trends to your historical baselines.")


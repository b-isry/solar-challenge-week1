import sys
import os

# Add the project root folder (one level above 'app') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from app.utils import fetch_data, get_top_regions

st.set_page_config(page_title = "Solar Challenge", page_icon = "🌞", layout = "wide")
st.title("Solar challenge")
st.markdown('This app is a simple dashboard to visualize the solar data for the countries in West Africa.')

df = fetch_data()

st.sidebar.header('Filters')
countries = df['country'].unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", countries, default = countries )
metric = st.sidebar.selectbox("Select Metric", ['GHI', 'DHI', 'DNI'])

df_filtered = df[df['country'].isin(selected_countries)]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f'Boxplot of {metric} by Country')
    fig, ax = plt.subplots(figsize = (8, 4))
    sns.boxplot(data = df_filtered, x = 'country', y = metric, ax = ax)
    st.pyplot(fig)
with col2:
    st.subheader(f'Top 5 regions by{metric}')
    top_regions = get_top_regions(df_filtered, metric = metric)
    st.dataframe(top_regions, use_container_width = True)
    
st.markdown('---')
st.caption('Made with ❤️ by b-isry')
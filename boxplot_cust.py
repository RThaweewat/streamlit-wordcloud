import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_pickle('rfm_results_cleaned.pkl')

clist = df['Segment'].unique()
segments = st.sidebar.selectbox("Select a segment:",clist)

st.header("GDP per Capita over time")
fig = px.box(df, x=segments, y="Recency", color="Churn")
fig.update_traces(quartilemethod="exclusive") 
st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_pickle('rfm_results_cleaned.pkl')

clist = df['segment2_lv1'].unique()
segments = st.sidebar.selectbox("Select a segment:",clist)

st.header("GDP per Capita over time")
fig = px.box(df[df['segment2_lv1'] == segments], x="Segment", y="Recency", color="Churn_group")
fig.update_traces(quartilemethod="exclusive") 
st.plotly_chart(fig)

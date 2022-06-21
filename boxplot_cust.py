import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_pickle('rfm_results_cleaned.pkl')

st.header("Boxplot for RFM Segmentation")

clist = df['segment2_lv1'].unique()
segments = st.selectbox("Select a segment:" ,clist)
metric = st.selectbox("By Metric:" , ('Recency', 'Monetary', 'Frequency'))
st.write('Data points:', len(df[df['segment2_lv1'] == segments]))

FMCG_rfm_level_agg = df[df['segment2_lv1'] == segments].groupby('Segment').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': ['mean', 'count']
}).round(1)

st.dataframe(FMCG_rfm_level_agg.style.highlight_max(axis=0))
st.subheader(f"RFM Segment in {segments} by {metric}")
fig = px.box(df[df['segment2_lv1'] == segments], x="Segment", y=metric, color="Churn_group", boxpoints = False)
fig.update_traces(quartilemethod="exclusive") 
st.plotly_chart(fig)

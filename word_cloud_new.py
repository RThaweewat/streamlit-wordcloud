import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title('Word Cloud Generator')
st. markdown("""
Author: Thaweewat, 28/4/2022
""")
st.set_option('deprecation.showPyplotGlobalUse', False)


# Create some sample text
Text = st.text_input('Text :', 'put text here')

st.sidebar.header("Select No. of words you want to display")
words = st.sidebar.selectbox("No. of words", range(10, 1000, 10))

# Create and generate a word cloud image:
wordcloud = WordCloud(background_color = "white", max_words = words).generate(Text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

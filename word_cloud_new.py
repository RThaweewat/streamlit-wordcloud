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
words = st.slider('Set maximum charactor: ', 10, 5000, 100)
st.write("Maximum words: ", words, 'Characters')

# Create and generate a word cloud image:
wordcloud = WordCloud(background_color = "white"
                      , max_words = words
                      , width=2000
                      , height=2000
                      , font_path='Kanit-Regular.ttf').generate(Text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()


import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pythainlp import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import pythainlp

st.title('Word Cloud Generator')
st. markdown("""
Author: Thaweewat, 28/4/2022
""")
st.set_option('deprecation.showPyplotGlobalUse', False)
regexp = r"[ก-๙a-zA-Z']+"

# Create some sample text
token = st.text_input('Text :', 'put text here')
Text = word_tokenize(token, keep_whitespace=False)
Text = TreebankWordDetokenizer().detokenize(Text)
st.write("Maximum words: ", Text, 'Characters')
st.sidebar.header("Select No. of words you want to display")
words = st.slider('Set maximum charactor: ', 10, 5000, 100)
st.write("Maximum words: ", words, 'Characters')


wordcloud = WordCloud(background_color = "white"
                      , max_words = words
                      , width=2000
                      , height=2000
                      , relative_scaling = 0.3
                      , colormap='plasma'
                      , collocations=False
                      , regexp=regexp
                      , margin=2
                      , font_path ='Kanit-Regular.ttf').generate(Text)


# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

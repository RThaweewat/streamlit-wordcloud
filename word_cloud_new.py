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
URL = st.text_input('URL:', 'put link here')
st.write('The current link is', URL)

st.sidebar.header("Select No. of words you want to display")
words = st.sidebar.selectbox("No. of words", range(10, 1000, 10))

if URL is not None:
    r = requests.get(URL)
    #using the web scraping library that is Beautiful Soup
    soup = BeautifulSoup(r.content, 'html.parser')
    #extracting the data that is in 'div' content of HTML page
    table = soup.find('div', attrs = {'id':'main-content'})
    text = table.text
    #cleaning the data with regular expression library
    cleaned_text = re.sub('\t', "", text)
    cleaned_texts = re.split('\n', cleaned_text)
    cleaned_textss = "".join(cleaned_texts)
    st.write("Word Cloud Plot")
    #using stopwords to remove extra words
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color = "white", max_words =
              words,stopwords = stopwords).generate(cleaned_textss)

# Display the generated image:
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
st.pyplot()

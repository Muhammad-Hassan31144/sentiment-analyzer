import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="main")

def sentiment_analyzer(text_to_analyze):
    nlp = load_model()
    result = nlp(text_to_analyze)
    label = result[0]['label']
    score = result[0]['score']
    return {'label': label, 'score': score}

st.title('Sentiment Analysis App')

text_to_analyze = st.text_area('Enter text to analyze:', '')

if st.button('Analyze'):
    if text_to_analyze:
        response = sentiment_analyzer(text_to_analyze)
        label = response['label']
        score = response['score']
        
        st.subheader('Results:')
        st.write(f"Label: {label}")
        st.write(f"Score: {score:.2f}")

        st.progress(score)

        if label == "POSITIVE":
            st.success("The sentiment is positive! This could indicate satisfaction or happiness.")
        elif label == "NEGATIVE":
            st.error("The sentiment is negative. This might indicate dissatisfaction or sadness.")
        else:
            st.info("The sentiment is neutral or mixed.")
    else:
        st.error('Please enter some text to analyze.')

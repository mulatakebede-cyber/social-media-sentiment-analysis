# app/main.py
import streamlit as st
from classify import classify_sentiment
from fetch_tweets import get_tweets

st.set_page_config(page_title="Social Media Sentiment Analysis", page_icon="📊", layout="wide")

st.title("📊 Social Media Sentiment Analysis")
st.write("Analyze tweets in real-time using OpenAI GPT sentiment classification.")

# Input keyword
keyword = st.text_input("Enter a keyword to fetch tweets:", "OpenAI")
count = st.slider("Number of tweets to fetch:", 5, 50, 10)

if st.button("Analyze Tweets"):
    with st.spinner("Fetching and analyzing tweets..."):
        try:
            tweets = get_tweets(keyword, count)
            results = [(tweet, classify_sentiment(tweet)) for tweet in tweets]

            # Display results
            st.subheader("Results")
            for text, sentiment in results:
                st.write(f"**Sentiment:** {sentiment}")
                st.write(f"Tweet: {text}")
                st.markdown("---")

        except Exception as e:
            st.error(f"Error: {e}")

# app/fetch_tweets.py
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

def get_tweets(keyword: str, count: int = 10):
    """
    Fetch recent tweets based on keyword.
    Requires Twitter developer credentials.
    """
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
    )
    api = tweepy.API(auth)

    tweets = api.search_tweets(q=keyword, lang="en", count=count, tweet_mode="extended")
    return [tweet.full_text for tweet in tweets]

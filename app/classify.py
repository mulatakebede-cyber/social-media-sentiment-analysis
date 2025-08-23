# app/classify.py
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_sentiment(text: str) -> str:
    """
    Classify sentiment of a given text using OpenAI.
    Returns one of: Positive, Negative, Neutral, Spam, Hate, Informative, Funny
    """
    categories = ["Positive", "Negative", "Neutral", "Spam", "Hate", "Informative", "Funny"]

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"You are a sentiment analysis classifier. Classify the following post into one of these categories: {', '.join(categories)}. Respond only with the category."},
            {"role": "user", "content": text}
        ],
        temperature=0
    )
    return response.choices[0].message["content"].strip()

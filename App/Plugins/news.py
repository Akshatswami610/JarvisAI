import os
import requests
from dotenv import load_dotenv

# Load secrets from .env file
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news():
    try:
        if not NEWS_API_KEY:
            return "News API key is missing. Please check your .env file."

        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url).json()
        articles = response.get("articles", [])
        if not articles:
            return "No news found."
        headlines = [a["title"] for a in articles[:5]]
        return "Here are the top headlines:\n" + "\n".join(headlines)
    except Exception as e:
        return f"Error fetching news: {e}"

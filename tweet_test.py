import os
import tweepy
from datetime import datetime
from dotenv import load_dotenv
# 以下箇所は取得したAPI情報と置き換えてください。
load_dotenv()  # Load default environment variables (.env)
API_KEY = os.getenv("API_KEY", "")
assert API_KEY, "API_KEY environment variable is missing from .env"

API_KEY_SECRET = os.getenv("API_KEY_SECRET", "")
assert API_KEY_SECRET, "API_KEY_SECRET environment variable is missing from .env"

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
assert ACCESS_TOKEN, "ACCESS_TOKEN environment variable is missing from .env"

ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", "")
assert ACCESS_TOKEN_SECRET, "ACCESS_TOKEN_SECRET environment variable is missing from .env"

dt_time = datetime.now().time()
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

tweet = "This is a test tweet from Python using Twitter API  " + str(dt_time)
response = client.create_tweet(text=tweet)
if response:
    print(response)
    # print(response)
else:
    print("error")

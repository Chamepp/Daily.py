import tweepy
from textblob import TextBlob

# Twitter API credentials (you need to create a Twitter Developer account to obtain these)
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

def analyze_tweet_sentiment(tweet):
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(tweet)
    
    # Determine sentiment polarity
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Input Twitter username and number of tweets to analyze
username = input("Enter Twitter username: ")
num_tweets = int(input("Enter number of tweets to analyze: "))

# Get user's timeline tweets
tweets = api.user_timeline(screen_name=username, count=num_tweets)

# Analyze sentiment for each tweet
for tweet in tweets:
    print("Tweet:", tweet.text)
    print("Sentiment:", analyze_tweet_sentiment(tweet.text))
    print()


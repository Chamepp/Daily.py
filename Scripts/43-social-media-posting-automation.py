import tweepy

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the tweet message
tweet_message = "Hello, Twitter! This is an automated tweet using Python and Tweepy. #Automation #PythonScript"

# Post the tweet
api.update_status(tweet_message)
print("Tweet posted successfully!")

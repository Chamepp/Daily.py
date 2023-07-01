import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    # Initialize the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Analyze the sentiment of the text
    sentiment_scores = sid.polarity_scores(text)

    # Determine the sentiment label based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment_label = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Return the sentiment score and label
    return sentiment_scores['compound'], sentiment_label

# Example usage
text_to_analyze = "I love this product! It's amazing!"
sentiment_score, sentiment_label = analyze_sentiment(text_to_analyze)
print(f"Sentiment Score: {sentiment_score}")
print(f"Sentiment Label: {sentiment_label}")

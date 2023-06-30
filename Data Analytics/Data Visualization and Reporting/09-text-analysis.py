import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download NLTK resources (run once)
nltk.download('vader_lexicon')
nltk.download('stopwords')

def preprocess_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Remove punctuation and non-alphabetic characters
    clean_tokens = [token for token in filtered_tokens if token.isalpha()]

    # Join the tokens back into a string
    processed_text = ' '.join(clean_tokens)

    return processed_text

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

def extract_keywords(text, num_keywords=5):
    # Tokenize the text into words
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Calculate the frequency distribution of tokens
    fdist = FreqDist(filtered_tokens)

    # Get the most frequent keywords
    keywords = fdist.most_common(num_keywords)

    return [keyword[0] for keyword in keywords]

# Example usage
text = "I absolutely love this movie! The plot was intriguing and the acting was superb."
preprocessed_text = preprocess_text(text)
sentiment_scores = perform_sentiment_analysis(preprocessed_text)
keywords = extract_keywords(preprocessed_text)

print("Preprocessed Text:", preprocessed_text)
print("Sentiment Scores:", sentiment_scores)
print("Keywords:", keywords)


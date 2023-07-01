from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

def text_summarization(text, num_sentences):
    # Tokenize the text into individual words
    words = word_tokenize(text.lower())

    # Remove stopwords (common words like "the", "is", etc.)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.casefold() not in stop_words]

    # Perform stemming to reduce words to their root form
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    # Calculate the frequency distribution of words
    word_frequencies = FreqDist(stemmed_words)

    # Sort the words based on their frequency
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

    # Extract the top 'num_sentences' most frequent words
    top_words = [word[0] for word in sorted_words[:num_sentences]]

    # Generate the summary by joining the top words into sentences
    summary = ' '.join(top_words)

    return summary

# Example usage
input_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed efficitur lorem auctor, blandit velit in, faucibus ipsum. Vivamus tincidunt mauris ut nisl tristique, et scelerisque purus interdum. Phasellus eu urna massa. Aliquam convallis dictum est, id aliquet dui hendrerit eget. Sed ullamcorper tincidunt lacinia. Mauris auctor lorem eget luctus venenatis. Duis tincidunt nunc sit amet eros ullamcorper placerat. Sed in lectus ac sapien tristique tincidunt. Sed viverra dignissim sapien, sit amet consectetur lorem dignissim a."

num_sentences = 2
summary = text_summarization(input_text, num_sentences)
print("Summary:")
print(summary)

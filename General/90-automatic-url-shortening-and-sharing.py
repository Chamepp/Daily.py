import pyshorteners

# Function to shorten and share a URL
def shorten_and_share_url(url):
    # Create a Shortener object
    shortener = pyshorteners.Shortener()

    try:
        # Shorten the given URL
        shortened_url = shortener.tinyurl.short(url)

        # Share the shortened URL
        share_on_social_media(shortened_url)

    except pyshorteners.exceptions.ShorteningErrorException:
        print("Error: Unable to shorten the URL.")

# Function to simulate sharing the URL on social media
def share_on_social_media(url):
    print("Sharing on social media:", url)
    # Add your code here to implement the actual sharing functionality

# Example usage
url = "https://www.example.com/your-long-url"
shorten_and_share_url(url)

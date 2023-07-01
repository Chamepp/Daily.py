import requests
import json

def get_instagram_analytics(username):
    # Set your Instagram API access token or use a library like instaloader for scraping
    access_token = "YOUR_INSTAGRAM_API_ACCESS_TOKEN"
    
    # Make a request to the Instagram API
    api_url = f"https://api.instagram.com/v1/users/self/media/recent/?access_token={access_token}"
    response = requests.get(api_url)
    data = json.loads(response.text)
    
    # Retrieve the desired metrics
    followers_count = data["data"][0]["user"]["followed_by"]["count"]
    likes_count = data["data"][0]["likes"]["count"]
    comments_count = data["data"][0]["comments"]["count"]
    shares_count = data["data"][0]["shares"]
    
    # Print the analytics
    print(f"Instagram Analytics for {username}:")
    print(f"Followers: {followers_count}")
    print(f"Likes: {likes_count}")
    print(f"Comments: {comments_count}")
    print(f"Shares: {shares_count}")

# Provide the Instagram username for which you want to fetch the analytics
username = "example_username"
get_instagram_analytics(username)

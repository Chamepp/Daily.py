import requests

def scrape_social_media_data(username):
    url = f"https://api.example.com/users/{username}/posts"  # Replace with the actual API endpoint

    # Add any necessary headers or authentication tokens for the API
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant data from the API response
        posts = data["posts"]
        comments = data["comments"]
        likes = data["likes"]

        # Process and analyze the data as needed
        # ...

        # Return the extracted data or perform additional operations
        return posts, comments, likes
    else:
        print("Error: Failed to fetch data from the social media API.")
        return None

# Example usage
username = input("Enter the username: ")
social_media_data = scrape_social_media_data(username)

if social_media_data:
    posts, comments, likes = social_media_data
    print(f"Found {len(posts)} posts, {len(comments)} comments, and {likes} likes for user {username}.")
else:
    print("Unable to retrieve social media data for the specified username.")


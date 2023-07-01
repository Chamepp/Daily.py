import random

# Define a list of movie or TV show genres
genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller"]

# Define a dictionary of recommended movies or TV shows based on genres
recommendations = {
    "Action": ["The Dark Knight", "Avengers: Endgame", "Mission: Impossible - Fallout"],
    "Adventure": ["Indiana Jones and the Raiders of the Lost Ark", "Jurassic Park", "The Lord of the Rings"],
    "Comedy": ["Anchorman: The Legend of Ron Burgundy", "Bridesmaids", "Superbad"],
    "Drama": ["The Shawshank Redemption", "The Godfather", "Pulp Fiction"],
    "Fantasy": ["Harry Potter and the Philosopher's Stone", "The Chronicles of Narnia", "Pan's Labyrinth"],
    "Horror": ["The Shining", "Get Out", "A Quiet Place"],
    "Mystery": ["Gone Girl", "Sherlock Holmes", "The Prestige"],
    "Romance": ["The Notebook", "La La Land", "Pride and Prejudice"],
    "Sci-Fi": ["Blade Runner 2049", "Interstellar", "The Matrix"],
    "Thriller": ["Inception", "Seven", "Fight Club"]
}

# Get user preferences for genres
print("Welcome to the Movie/TV Show Recommendation Generator!")
print("Please select your preferred genres (separated by commas):")
user_genres = input().split(',')

# Remove any whitespace around the user's preferences
user_genres = [genre.strip() for genre in user_genres]

# Filter the recommended movies or TV shows based on user preferences
filtered_recommendations = [recommendations[genre] for genre in user_genres if genre in recommendations]

# Check if there are any recommendations for the user's preferred genres
if filtered_recommendations:
    # Select a random movie or TV show from the filtered recommendations
    random_recommendation = random.choice(filtered_recommendations[0])
    print("Based on your preferences, we recommend watching:", random_recommendation)
else:
    print("Sorry, no recommendations available for your preferred genres.")

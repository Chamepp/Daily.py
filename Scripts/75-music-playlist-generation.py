import random

# List of songs
songs = [
    "Song 1",
    "Song 2",
    "Song 3",
    "Song 4",
    "Song 5",
    "Song 6",
    "Song 7",
    "Song 8",
    "Song 9",
    "Song 10"
]

# User preferences (genres, artists, etc.)
user_preferences = [
    "Genre 1",
    "Artist 2",
    "Genre 3"
]

# Function to generate a music playlist
def generate_playlist(songs, preferences):
    playlist = []
    for song in songs:
        # Check if the song matches any user preference
        for preference in preferences:
            if preference in song:
                playlist.append(song)
                break
    return playlist

# Generate and print the playlist
playlist = generate_playlist(songs, user_preferences)
print("Your music playlist:")
for song in playlist:
    print(song)

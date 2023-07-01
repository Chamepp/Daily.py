import lyricsgenius

def fetch_lyrics(artist, song_title):
    # Replace 'YOUR_ACCESS_TOKEN' with your own Genius API access token
    genius = lyricsgenius.Genius('YOUR_ACCESS_TOKEN')

    # Search for the song lyrics
    song = genius.search_song(song_title, artist)

    if song is not None:
        return song.lyrics
    else:
        return "Lyrics not found."

# Example usage
artist = "Ed Sheeran"
song_title = "Shape of You"
lyrics = fetch_lyrics(artist, song_title)
print(lyrics)

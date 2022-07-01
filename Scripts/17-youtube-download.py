import sys
import youtube_dl


# Defining Download Method
def download_youtube(url):
    # Importing Function As Ydl
    with youtube_dl.YoutubeDL() as ydl:

        # Try Downloading Video
        try:
            retcode = ydl.download([url])

        # Maximum Download Exception
        except youtube_dl.MaxDownloadsReached:
            ydl.to_screen('--max-download limit reached, aborting.')
            retcode = 101

    return retcode

# Data
url = 'sample'
code = download_youtube(url)

# Exit
sys.exit(code)

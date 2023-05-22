import requests

def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded file '{filename}' successfully!")
    else:
        print(f"Failed to download file from '{url}'.")

# Example usage
url = 'https://example.com/file.txt'
filename = 'downloaded_file.txt'
download_file(url, filename)

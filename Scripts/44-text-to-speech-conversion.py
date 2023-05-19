from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, language='en'):
    speech = gTTS(text=text, lang=language)
    speech.save('output.mp3')  # Save the speech as an MP3 file

    # Play the speech
    os.system('mpg123 output.mp3')  # You can replace 'mpg123' with your preferred audio player command

# Prompt the user for input
text = input("Enter the text to convert to speech: ")

# Convert the input text to speech
text_to_speech(text)

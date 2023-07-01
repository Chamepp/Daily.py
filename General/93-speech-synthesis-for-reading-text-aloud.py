import pyttsx3

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set the properties for the speech
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)
    
    # Say the given text aloud
    engine.say(text)
    engine.runAndWait()

# Example usage
text = "Hello, world! This is a test."
text_to_speech(text)

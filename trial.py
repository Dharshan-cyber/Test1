import pyttsx3
#hi da
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech (default: 200)
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)  # Convert text to speech
    engine.runAndWait()  # Play the speech

# Example usage
a=input("enter text: ")
text_to_speech(a)

#trial

#hiuhihdiuahsiudhdbfkusvfuskdvfuk


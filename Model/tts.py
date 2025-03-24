import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed
    engine.setProperty('volume', 1.0)  # Adjust volume
    engine.say(text)
    engine.runAndWait()

# Example usage:
# text_to_speech("Hello! How can I help you?")

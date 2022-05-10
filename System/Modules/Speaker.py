import pyttsx3
from System.Modules.BootLoader import Config

config = Config()

class Speaker():
    def __init__(self):
        # init function to get an engine instance for the speech synthesis
        if config.providers_text_to_speech == "pyttsx3":
            self.engine = pyttsx3.init()
    
    def speak(self, text):
        # say method on the engine that passing input text to be spoken
        self.engine.say(text)

        # run and wait method, it processes the voice commands.
        self.engine.runAndWait()

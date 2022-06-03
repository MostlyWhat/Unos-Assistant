
import requests
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Initialising Modules
config = Config()
crisis = Crisis()

class Preburner():
    def __init__(self):
      pass

    def start(self):
      pass

class PreChecks():
    def __init__(self):
        self.config = Config()

    def check(self):
        # Check Internet Connection
        self.InternetCheck()
        self.Configurations()
        self.InterfaceType()

    @staticmethod
    def InternetCheck():
        # Check Internet Connection
        url = "https://ismyinternetworking.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            crisis.log(
                "PreChecks",
                "Successfully connected to the Internet")
            return True

        except Exception:
            crisis.log(
                "PreChecks",
                "Failed to Connect to the Internet")
            return False

    @staticmethod
    def InterfaceType():
        interface_type = config.launch_mode

        if interface_type == "cli":
            crisis.log(
                "Interface",
                "Loading Command Line Interface")

        elif interface_type == "gui":
            crisis.log(
                "Interface",
                "Loading Graphical User Interface")

        elif interface_type == "web":
            crisis.log(
                "Interface",
                "Loading Web Interface and Server")

        else:
            crisis.warning(
                "Interface", "Unknown Interface Configuration")
            crisis.log(
                "Interface",
                "Defaulting back to Command Line Interface")
            crisis.log(
                "Interface",
                "Loading Command Line Interface")

    @staticmethod
    def Configurations():
        dev_mode = config.dev_mode

        # Checking if the dev_mode is enabled
        if dev_mode is True:
            crisis.log(
                "PreChecks",
                "Development Mode is Enabled")

        else:
            crisis.log(
                "PreChecks",
                "Development Mode is Disabled")

        # Checking on what features are enabled
        text_to_speech = config.text_to_speech
        voice_recognition = config.voice_recognition

        if text_to_speech is True:
            crisis.log(
                "PreChecks",
                "Text to Speech is Enabled")

        else:
            crisis.log(
                "PreChecks",
                "Text to Speech is Disabled")

        if voice_recognition is True:
            crisis.log(
                "PreChecks",
                "Voice Recognition is Enabled")

        else:
            crisis.log(
                "PreChecks",
                "Voice Recognition is Disabled")

import concurrent.futures

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Speech import Listener, Speaker
from System.Modules.Splitter import Splitter

# Module Information
# Module Name: System.Modules.Interface
# Module Purpose: To Provide the Interface for the UNOS Assistant Framework

# Setting Up Modules
config = Config()
crisis = Crisis()

# Setup if the user enabled text to speech and if they did not, then disable it
if config.text_to_speech is True:
    speaker = Speaker()

# Setup if the user enabled voice recognition and if they did not, then disable it
if config.voice_recognition is True:
    listener = Listener()

modules = [f"{config.analyzers_location}.{modules}" for modules in config.analyzers_modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

# Quick Variables
unos_name = config.unos_name
username = config.username
launch_config = config.launch_mode

# Interface Modules
class Interface():
    @staticmethod
    def start():
        if launch_config == "cli" and config.voice_recognition is True:
            cli_interface = cli_speech()
            cli_interface.main()

        elif launch_config == "gui":
            gui_interface = gui()
            gui_interface.main()

        elif launch_config == "web":
            web_interface = web()
            web_interface.main()

        else:
            cli_interface = cli()
            cli_interface.main()

    @staticmethod
    def moreinfo():
        if launch_config == "cli" and config.voice_recognition is True:
            cli_interface = cli_speech()
            return cli_interface.extra_input()

        elif launch_config == "gui":
            gui_interface = gui()
            return gui_interface.extra_input()

        elif launch_config == "web":
            web_interface = web()
            return web_interface.extra_input()

        else:
            cli_interface = cli()
            return cli_interface.extra_input()

class cli():
    def main(self):
        try:            
            # Gets Input from Splitter
            print(" ")
            query = str(input(f"{username}@{unos_name}: "))
            print(" ")
            splitter_output = splitter.analyze(query)

            # Outputting the Results
            self.outputting(splitter_output)

        except Exception as e:
            crisis.error(
                "Interface", f"The Error: {e} has occurred")

    def extra_input(self):
        extrainput_request = "I'm sorry, can you provide me with a category?"

        if config.text_to_speech is True:
            speaker.speak(extrainput_request)

        self.outputting(extrainput_request)
        print(" ")
        response = str(input(f"{username}@{unos_name}: "))
        print(" ")

        return response

    @staticmethod
    def outputting(splitter_output: str):
        # Printing the Results
        print(f"[ {unos_name.upper()} ] {splitter_output}")

        # Run the Speaker Module in another thread, interruptable
        if config.text_to_speech is True:
            speaker.speak(splitter_output)

class cli_speech():
    def main(self):
        try:
            # Listen for Wakeup Call
            print(f"\n[ {unos_name.upper()} ] Listening for Wakeup Command...")
            listen = listener.listenForUNOS()

            # If the wakeup call is detected, then ask for input
            if listen is True:
                if config.text_to_speech is True:
                    speaker.speak("Yes?")

                print(f"\n[ {unos_name.upper()} ] Listening for Command...")
                user_response = listener.listenForCommand()

                # Send the Input to Splitter for Analysis
                print(f"\n[ {unos_name.upper()} ] {username} responded with: {user_response}")
                splitter_output = splitter.analyze(user_response)

                # Outputting the Results
                self.outputting(splitter_output)

        except Exception as e:
            crisis.error(
                "Interface", f"The Error: {e} has occurred")

    def extra_input(self):
        pass

    @staticmethod
    def outputting(splitter_output: str):
        # Printing the Results
        print(" ")
        print(f"[ {unos_name.upper()} ] {splitter_output}")

        # Run the Speaker Module in another thread, interruptable
        if config.text_to_speech is True:
            speaker.speak(splitter_output)

class gui():
    def main(self):
        pass

    def extra_input(self):
        pass

    def outputting(self):
        pass

class web():
    def main(self):
        pass

    def extra_input(self):
        pass

    def outputting(self):
        pass

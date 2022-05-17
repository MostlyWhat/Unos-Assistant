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

if config.text_to_speech is True:
    speaker = Speaker()
    
if config.voice_recognition is True:
    listener = Listener()

modules = [f"{config.modules_location}.{modules}" for modules in config.modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

class VoiceInterrupt(Exception):
    pass

# Interface Modules
class Interface():
    def __init__(self, configuration: str, username: str, unos_name: str):
        self.launch_config = configuration
        self.username = username
        self.unos_name = unos_name

    def start(self):
        if self.launch_config == "cli" or self.launch_config not in ["gui", "web"]:
            cli_interface = cli()
            cli_interface.main(self.username, self.unos_name)

        elif self.launch_config == "gui":
            gui_interface = gui()
            gui_interface.main(self.username, self.unos_name)

        else:
            web_interface = web()
            web_interface.main(self.username, self.unos_name)


class cli():
    def main(self, username: str, unos_name: str):
        try:
            if config.voice_recognition is True:
                # Starts a thread to listen for user input
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.submit(listener.listen)
            
            # Gets Input from Splitter
            print(" ")
            query = str(input(f"{username}@{unos_name}: "))
            print(" ")
            splitter_output = splitter.analyze(query)

            # Outputting the Results
            self.outputting(unos_name, splitter_output)
        
        except Exception as e:
            crisis.error(
                "UNOS Assistant Framework", f"An Unknown Error has occurred: {e}")

    def outputting(self, unos_name: str, splitter_output: str):
        # Printing the Results
        print(f"[ {unos_name.upper()} ] {splitter_output}")
        
        # Run the Speaker Module in another thread, interruptable
        if config.text_to_speech is True:
            speaker.speak(splitter_output)

class gui():
    def main(self, username: str, unos_name: str):
        pass


class web():
    def main(self, username: str, unos_name: str):
        pass

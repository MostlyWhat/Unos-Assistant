import multiprocessing
from threading import Thread

import keyboard
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Speaker import Speaker
from System.Modules.Splitter import Splitter

# Module Information
# Module Name: System.Modules.Interface
# Module Purpose: To Provide the Interface for the UNOS Assistant Framework

# Setting Up Modules
config = Config()
crisis = Crisis()
speaker = Speaker()

modules = [f"{config.modules_location}.{modules}" for modules in config.modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

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
            print(" ")
            query = str(input(f"{username}@{unos_name}: "))
            print(" ")
            splitter_output = splitter.analyze(query)

            # Printing the Results
            print(f"[ {unos_name.upper()} ] {splitter_output}")
            
            # Run the Speaker Module in another thread, interruptable
            speaker.speak(splitter_output)
        
        except Exception as e:
            crisis.error(
                "UNOS Assistant Framework", f"An Unknown Error has occurred: {e}")


class gui():
    def main(self, username: str, unos_name: str):
        pass


class web():
    def main(self, username: str, unos_name: str):
        pass

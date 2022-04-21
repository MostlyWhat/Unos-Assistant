
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Splitter import Splitter

# Module Information
# Module Name: System.Modules.Interface
# Module Purpose: To Provide the Interface for the UNOS Assistant Framework

# Setting Up Modules
config = Config()
crisis = Crisis()

modules = [f"{config.modules_location}.{modules}" for modules in config.modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

# Interface Modules


class Interface():
    def __init__(self, configuration: str, username: str, unos_name: str):
        self.launch_config = configuration
        self.username = username
        self.unos_name = unos_name

    def start(self):
        if self.launch_config == "cli":
            cli.main(self.username, self.unos_name)

        elif self.launch_config == "gui":
            gui.main(self.username, self.unos_name)

        elif self.launch_config == "web":
            web.main(self.username, self.unos_name)

        else:
            cli.main(self.username, self.unos_name)


class cli():
    def main(username: str, unos_name: str):
        try:
            print(" ")
            query = str(input(f"{username}@{unos_name}: "))
            print(" ")
            print(f"[ {unos_name.upper()} ] {splitter.analyze(query)}")

        except Exception as e:
            crisis.error(
                "UNOS Assistant Framework", f"An Unknown Error has occurred: {e}")


class gui():
    def main(username: str, unos_name: str):
        pass


class web():
    def main(username: str, unos_name: str):
        pass

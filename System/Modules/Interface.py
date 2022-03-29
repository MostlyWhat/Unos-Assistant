from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Splitter import Splitter

# Setting Up Modules
config = Config()
crisis_handler = Crisis()


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
            crisis_handler.log(
                "Interface",
                "Loading Command Line Interface")
            cli.main(self.username, self.unos_name)

        elif self.launch_config == "gui":
            crisis_handler.log(
                "Interface",
                "Loading Graphical User Interface")
            gui.main(self.username, self.unos_name)

        elif self.launch_config == "web":
            crisis_handler.log(
                "Interface",
                "Loading Web Interface and Server")
            web.main(self.username, self.unos_name)

        else:
            crisis_handler.warning(
                "Interface: Unknown Interface Configuration")
            crisis_handler.log("Interface > Defaulting to CLI")
            cli.main(self.username, self.unos_name)


class cli():
    def main(username: str, unos_name: str):
        try:
            query = str(input(f"{username}@{unos_name}: "))
            print(f"UNOS: {splitter.analyze(query)}")

        except Exception as e:
            print(f"Interface > An Error has occured: {e}")


class gui():
    def main(username: str, unos_name: str):
        pass


class web():
    def main(username: str, unos_name: str):
        pass

import importlib

from System.Modules.BootLoader import Config

# Setting up System Modules
config = Config()

class Splitter():
    def __init__(self, fallback_module: str, plugins: list = None):
        if plugins is None:
            plugins = []
        self.fallback_module = fallback_module
        # Checking if plugin were set
        if plugins != []:
            # create a list of plugins
            self._plugins = [
                # Import the module and initialise it at the same time
                importlib.import_module(plugin, ".").Plugin() for plugin in plugins
            ]
        else:
            # If no plugin were set we use our default
            self._plugins = [importlib.import_module(
                f"System.Analysis.{fallback_module}", ".") .Plugin()]

    def analyze(self, query: str):
        adaptors = []

        # Analyze using other plugins
        for plugin in self._plugins:
            responses = plugin.analyze(query)

            if responses is True:
                adaptors.append(plugin.name)

        if len(adaptors) > 1:
            print("Multiple adaptors found, please select one:")
            for i, adaptor in enumerate(adaptors):
                print(f"{i}: {adaptor}")

            choice = int(input("Choice: "))
            adaptors = [adaptors[choice]]

        else:
            adaptors.append(f"System.Analysis.{self.fallback_module}")


        selected_adaptor = importlib.import_module(
            str(adaptors[0]), ".").Plugin()

        return selected_adaptor.process(query)

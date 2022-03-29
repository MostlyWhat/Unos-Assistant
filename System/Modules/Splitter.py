import importlib
from unicodedata import category


class Splitter():
    def __init__(self, fallback_module: str, plugins: list = []):
        self.fallback_module = fallback_module
        # Checking if plugin were sent
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

            if responses == True:
                adaptors.append(plugin.name)

        if len(adaptors) == 0:
            adaptors.append(f"System.Analysis.{self.fallback_module}")

        elif len(adaptors) > 1:
            self.context_request(query, adaptors)

        selected_adaptor = importlib.import_module(
            str(adaptors[0]), ".").Plugin()

        return selected_adaptor.process(query)

    def context_request(self, query: str, adaptors: str):
        pass
        # Returns 1 Adaptor

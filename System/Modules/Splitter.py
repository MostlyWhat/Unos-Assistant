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
                f"{config.fallback_location}.{self.fallback_module}", ".") .Plugin()]

    def analyze(self, query: str):        
        adaptors = []

        # Analyze using other plugins
        for plugin in self._plugins:
            responses = plugin.analyze(query)

            if responses is True:
                adaptors.append(f"{config.analyzers_location}.{plugin.name}")

        if len(adaptors) > 1:
            adaptors = self.multipleAdaptors(adaptors)

        else:
            adaptors.append(f"{config.fallback_location}.{self.fallback_module}")

        selected_adaptor = importlib.import_module(f"{str(adaptors[0])}", ".").Plugin()

        return selected_adaptor.process(query)

    @staticmethod
    def multipleAdaptors(adaptors):        
        from System.Modules.Interface import Interface
        context = Interface().moreinfo()

        for adaptor in adaptors:
            check = importlib.import_module(f"{str(adaptor)}", ".").Plugin().analyze(context)

            if check is True:
                return [adaptor]

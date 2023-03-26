import importlib

from System.Modules.BootLoader import Config

# Setting up System Modules
config = Config()

# > Splitter is a class that splits a string into a list of words
class Splitter():
    def __init__(self, fallback_module: str, plugins: list = None):
        """
        If plugins is not None, then create a list of plugins, otherwise create a list of fallback
        plugins
        
        :param fallback_module: str = "fallback"
        :type fallback_module: str
        :param plugins: list = None
        :type plugins: list
        """
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
        """
        It takes a query, analyzes it using other plugins, and returns the best plugin to use
        
        :param query: The query to be analyzed
        :type query: str
        :return: The return value of the process method of the selected adaptor.
        """
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
        """
        It imports a module from a string, and then calls a function from that module
        
        :param adaptors: A list of adaptors to check
        :return: The adaptor that is being returned is the one that is being used to analyze the
        context.
        """
        from System.Modules.Interface import Interface
        context = Interface().moreinfo()

        for adaptor in adaptors:
            check = importlib.import_module(f"{str(adaptor)}", ".").Plugin().analyze(context)

            if check is True:
                return [adaptor]

from System.Modules.BootLoader import Config

# Module Information
# Module Name: System.Analysis.Exit
# Module Purpose: To Provide the Exit for the UNOS Assistant Framework

# Setting Up Configurations
config = Config()

class Plugin:
    def __init__(self):
        self.name = "Exit"
        self.contexts = ["exit", "quit", "shutdown", "shut down"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    @staticmethod
    def process(query):
        raise KeyboardInterrupt

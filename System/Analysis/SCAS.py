# Define our default class
class Plugin:
    def __init__(self):
        self.name = "System.Analysis.SCAS"
        self.contexts = []

    # Define static method, so no self parameter
    def analyze(self, query):
        # Some prints to identify which plugin is been used

        return False

    def process(self, query):
        return "Processing Here SCAS"

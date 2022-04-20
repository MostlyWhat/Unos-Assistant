class Plugin:
    def __init__(self):
        self.name = "System.Analysis.SCAS"
        self.contexts = []

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        return "Processing Here SCAS"

class Plugin:
    def __init__(self):
        self.name = "SCAS"
        self.contexts = []

    @staticmethod
    def analyze(query):
        # Set to True because we want to use the fallback module
        return True

    @staticmethod
    def process(self, query):
        return "Processing Here SCAS"

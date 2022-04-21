import random
from datetime import datetime


# Define our default class
class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Time"
        # Contexts that this plugin can handle
        self.contexts = ["time", "clock", "watch", "alarm"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    @staticmethod
    def process(query):
        prefix = ["The time is ", "The current time is ", "Currently it is "]
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        return random.choice(prefix) + current_time

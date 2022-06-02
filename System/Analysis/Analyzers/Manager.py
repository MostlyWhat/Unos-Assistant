from System.Modules.Management import Updater

# Setting Up Modules
updater = Updater()

class Plugin:
    def __init__(self):
        self.name = "Manager"
        self.contexts = ["update", "activate", "deactivate"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        if query.startswith("update"):
            command = query.split(" ")[1]
            return self.update(command)

        elif query.startswith("activate"):
            command = query.split(" ")[1]
            return self.protocol(command)

    @staticmethod
    def update(command):
        retrain = updater.regen(command)
        if retrain is True:
            return f"Sucessfully Regenerated the {command} Database"

        else:
            return f"Failed to Regenerate the {command} Database"

    def protocol(self, command):
        pass

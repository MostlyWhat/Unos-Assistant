from System.Modules.Management import Updater

# Setting Up Modules
updater = Updater()

class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Afterburner"
        self.contexts = ["update"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        # Remove the first word from the query
        command = query[7:len(query)]
        
        retain = updater.regen(command)
        if retain is True:
            return f"Sucessfully Regenerated the {command} Database"
    
        else:
            return f"Failed to Regenerate the {command} Database"

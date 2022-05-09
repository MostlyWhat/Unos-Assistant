from System.Modules.Management import Manager

# Setting Up Modules
manager = Manager()

class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Afterburner"
        self.contexts = ["manager"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        command = query.replace("manager regenerate ", "")
        retain = manager.regen(command)
        if retain is True:
            return f"Sucessfully Regenerated the {command} Database"
        
        else:
            return f"Failed to Regenerate the {command} Database"

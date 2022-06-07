from System.Modules.Management import Updater

# Setting Up Modules
updater = Updater()

class Plugin:
    def __init__(self):
        self.name = "Manager"
        self.contexts = ["update", "clear", "activate", "deactivate"]

    def analyze(self, query):
        return any((context in query for context in self.contexts))

    def process(self, query):
        if query.startswith("update"):
            command = query.split(" ")[1]
            return self.update(command)

        elif query.startswith("clear"):
            command = query.split(" ")[1]
            return self.clear(command)
        
        elif query.startswith("activate"):
            command = query.split(" ")[1]
            return self.protocol(command)

    @staticmethod
    def update(command):
        retrain = updater.update(command)
        if retrain is True:
            return f"Sucessfully Updated System Files from the {command} settings."

        else:
            return f"Failed to Update System Files from the {command} settings."

    @staticmethod
    def clear(command):
        clean = updater.clear(command)
        if clean is True:
            return f"Sucessfully Cleared System Files from the {command} settings."
        
        else:
            return f"Failed to Clear System Files from the {command} settings."

    @staticmethod
    def protocol(self, command):
        pass

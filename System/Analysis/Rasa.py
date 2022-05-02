import requests
from System.Modules.Crisis import Crisis
from urllib3 import HTTPConnectionPool

crisis = Crisis()


# Adaptor for Rasa Assistant Server
class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Rasa"
        self.contexts = []

    def analyze(self, query):
        # Fallback Plugin
        return True

    def process(self, query):
        sender = "Unos"
        try:
            r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": query})

            for i in r.json():
                bot_message = i['text']
                
            return bot_message

        except Exception as e:
            crisis.error("RasaAPI", "Error: " + str(e))
            return "No message was returned, check if the server has fully started."

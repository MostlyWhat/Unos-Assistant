import http.client
import json

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Module Information
config = Config()
crisis = Crisis()


class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Scraper"
        self.contexts = ["web", "search"]

    def analyze(self, query):
        can_process = True

        try:
            self.request_result(query)

        except Exception as e:
            crisis.error("Scraper", e)
            return False

        return any((context in query for context in self.contexts))

    def process(self, query):
        for words in self.contexts:
            question = query.replace(f"{words} ", "")

        return self.request_result(question)

    def request_result(self, query):
        question = query.replace(" ", "%20")

        conn = http.client.HTTPSConnection(config.rapidapi_host)

        headers = {
            "X-RapidAPI-Host": config.rapidapi_host,
            "X-RapidAPI-Key": config.rapidapi_api
        }

        conn.request(
            "GET", f"/?q={question}&callback=process_duckduckgo&no_html=1&no_redirect=1&skip_disambig=1&format=json", headers=headers)

        res = conn.getresponse()
        data = res.read()

        output = data.decode("utf-8")
        format_output = json.loads(output[19:len(output)-2])

        if format_output["AbstractText"] != "":
            return "According to " + format_output["AbstractSource"] + ", " + format_output["AbstractText"]

        crisis.error("Scraper", "No results found")
        return False

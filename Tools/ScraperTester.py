from System.Analysis.Analyzers.Scraper import Plugin
from System.Modules.BootLoader import Config

config = Config()
scraper = Plugin()

query = str(input("Query: "))
print(scraper.request_result(query))

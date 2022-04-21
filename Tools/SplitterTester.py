from System.Modules.BootLoader import Config
from System.Modules.Splitter import Splitter

# Tools Information
"""
Filename: SplitterTester.py
Purpose: Test the Splitter Module
Intended Usage: Put into root folder and input query

"""

# Setting Up Modules
username = "mostlywhat"
unos_name = "splitter"
config = Config()
modules = [f"{config.modules_location}.{modules}" for modules in config.modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

while True:
    query = str(input(f"{username}@{unos_name}: "))

    if query == 'exit':
        break
    print(f"UNOS: {splitter.analyze(query)}")

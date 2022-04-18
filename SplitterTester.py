from System.Modules.BootLoader import Config
from System.Modules.Splitter import Splitter

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

    else:
        print(f"UNOS: {splitter.analyze(query)}")

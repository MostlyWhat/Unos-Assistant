import os
import subprocess

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Splitter import Splitter

# Initialising Modules
config = Config()
crisis = Crisis()
modules = [f"{config.modules_location}.{modules}" for modules in config.modules]
splitter = Splitter(plugins=modules, fallback_module=config.fallback_module)

class Preburner():
    def __init__(self):
      self.fallback_module = config.fallback_module
      
    def start(self):
      pass
        # if self.fallback_module == "MCAS":
        #     crisis.log("Preburner", "Initialising MCAS")
        #     splitter.analyze("hello")
        #     crisis.log("Preburner", "MCAS is Online")

import os
import subprocess

import requests
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis
from System.Modules.Splitter import Splitter

# Initialising Modules
config = Config()
crisis = Crisis()

class Preburner():
    def __init__(self):
      pass
      
    def start(self):
      pass

class PreChecks():
    def __init__(self):
        self.config = Config()
    
    def check(self):
        # Check Internet Connection
        self.InternetCheck()
        self.InterfaceType()

    @staticmethod
    def InternetCheck():
        # Check Internet Connection
        url = "https://ismyinternetworking.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            crisis.log(
                "PreChecks",
                "Successfully connected to the Internet")
            crisis.log(
                "PreChecks",
                "Success: Code {0}".format(request.status_code))
            return True

        except Exception:
            crisis.log(
                "PreChecks",
                "Failed to Connect to the Internet")
            crisis.log("PreChecks", 'Error: Code 0'.format(request.status_code))
            return False

    @staticmethod
    def InterfaceType():
        interface_type = config.launch_mode

        if interface_type == "cli":
            crisis.log(
                "Interface",
                "Loading Command Line Interface")

        elif interface_type == "gui":
            crisis.log(
                "Interface",
                "Loading Graphical User Interface")

        elif interface_type == "web":
            crisis.log(
                "Interface",
                "Loading Web Interface and Server")

        else:
            crisis.warning(
                "Interface", "Unknown Interface Configuration")
            crisis.log(
                "Interface",
                "Defaulting back to Command Line Interface")
            crisis.log(
                "Interface",
                "Loading Command Line Interface")

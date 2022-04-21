
import requests
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Module Information
# Module Name: System.Modules.Pre-Checks
# Module Purpose: To Provide the Pre-Checks for the UNOS Assistant Framework

# Setting Up Configurations
config = Config()
crisis = Crisis()


class PreChecks():
    def __init__(self) -> None:
        pass

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
                "BootLoader",
                "Successfully connected to the Internet")
            return True

        except (requests.ConnectionError, requests.Timeout) as exception:
            crisis.log(
                "BootLoader",
                "Failed to Connect to the Internet")
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

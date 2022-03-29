import os
import random
import time
from pathlib import Path

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Setting up Modules
crisis_handler = Crisis()
config = Config()


class Boot():
    def __init__(self, configuration: str, username: str, unos_name: str):
        self.launch_config = configuration
        self.username = username
        self.unos_name = unos_name

    def show(self):
        if self.launch_config == "cli":
            crisis_handler.log(
                "Interface",
                "Loading Command Line Interface")
            self.cli(self.username, self.unos_name)

        elif self.launch_config == "gui":
            crisis_handler.log(
                "Interface",
                "Loading Graphical User Interface")
            self.gui(self.username, self.unos_name)

        elif self.launch_config == "web":
            crisis_handler.log(
                "Interface",
                "Loading Web Interface and Server")
            self.web(self.username, self.unos_name)

        else:
            crisis_handler.warning(
                "Interface: Unknown Interface Configuration")
            crisis_handler.log("Interface > Defaulting to CLI")
            self.cli(self.username, self.unos_name)

    def cli(self, username: str, unos_name: str):
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("System/Extras/boot_sequence.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0, 0.10))

        print("\n")

    def gui(self):
        pass

    def web(self):
        pass


class Splash():
    def __init__(self, configuration: str, username: str, unos_name: str):
        self.launch_config = configuration
        self.username = username
        self.unos_name = unos_name

    def show(self):
        if self.launch_config == "cli":
            crisis_handler.log(
                "Interface",
                "Loading Command Line Interface")
            self.cli()

        elif self.launch_config == "gui":
            crisis_handler.log(
                "Interface",
                "Loading Graphical User Interface")
            self.gui()

        elif self.launch_config == "web":
            crisis_handler.log(
                "Interface",
                "Loading Web Interface and Server")
            self.web()

        else:
            crisis_handler.warning(
                "Interface: Unknown Interface Configuration")
            crisis_handler.log("Interface > Defaulting to CLI")
            self.cli()

    def cli(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("System/Extras/unos_logo.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0, 0.10))

        print("\n")

        startup_lines = ["[ UNOS Assistant Framework ] Loading Configurations", " ", f"Assistant Name: {config.unos_name}", f"Assistant Version: {config.unos_version}",
                         f"Assistant Codename: {config.unos_codename}", f"Assistant Stability: {config.unos_stability}", f"Previous Interation: {config.unos_previous_interation}"]

        for line in startup_lines:
            print(line, end="\n")
            time.sleep(random.uniform(0, 0.10))

    def gui(self, username: str, unos_name: str):
        pass

    def web(self, username: str, unos_name: str):
        pass


class Exit():
    def __init__(self, configuration: str):
        self.launch_config = configuration

    def show(self):
        if self.launch_config == "cli":
            crisis_handler.log(
                "Interface",
                "Loading Command Line Interface")
            self.cli()

        elif self.launch_config == "gui":
            crisis_handler.log(
                "Interface",
                "Loading Graphical User Interface")
            self.gui()

        elif self.launch_config == "web":
            crisis_handler.log(
                "Interface",
                "Loading Web Interface and Server")
            self.web()

        else:
            crisis_handler.warning(
                "Interface: Unknown Interface Configuration")
            crisis_handler.log("Interface > Defaulting to CLI")
            self.cli()

    def cli(self):
        pass

    def gui(self):
        pass

    def web(self):
        pass

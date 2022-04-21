import os
import random
import time

from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Setting up Modules
crisis = Crisis()
config = Config()


class Boot():
    def __init__(self, configuration: str):
        self.launch_config = configuration

    def show(self):
        # if self.launch_config == "cli":
        #     self.cli()

        # elif self.launch_config == "gui":
        #     self.gui()

        # elif self.launch_config == "web":
        #     self.web()

        # else:
        #     self.cli()

        self.cli()

    @staticmethod
    def cli():
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("System/Extras/boot_sequence.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0, 0.10))

        print("\n")

    # def gui():
    #     pass

    # def web():
    #     pass


class Splash():
    def __init__(self, configuration: str):
        self.launch_config = configuration

    def show(self):
        # if self.launch_config == "cli":
        #     self.cli()

        # elif self.launch_config == "gui":
        #     self.gui()

        # elif self.launch_config == "web":
        #     self.web()

        # else:
        #     self.cli()

        self.cli()

    @staticmethod
    def cli():
        os.system('cls' if os.name == 'nt' else 'clear')

        boot_sequence = open("System/Extras/unos_logo.txt")
        boot_text = boot_sequence.readlines()
        for line in boot_text:
            print(line, end="")
            time.sleep(random.uniform(0, 0.10))

        print("\n")

        crisis.log("UNOS Assistant Framework", "Loading Configurations")

        startup_lines = [" ", f"[\tAssistant Name\t\t] {config.unos_name}", f"[\tAssistant Version\t] {config.unos_version}",
                         f"[\tAssistant Codename\t] {config.unos_codename}", f"[\tAssistant Stability\t] {config.unos_stability}", f"[\tPrevious Interation\t] {config.unos_previous_interation}"]

        for line in startup_lines:
            print(line, end="\n")
            time.sleep(random.uniform(0, 0.10))

    # def gui():
    #     pass

    # def web():
    #     pass


class Exit():
    def __init__(self, configuration: str):
        self.launch_config = configuration

    def show(self):
        # if self.launch_config == "cli":
        #     self.cli()

        # elif self.launch_config == "gui":
        #     self.gui()

        # elif self.launch_config == "web":
        #     self.web()

        # else:
        #     self.cli()

        self.cli()

    @staticmethod
    def cli():
        os.system('cls' if os.name == 'nt' else 'clear')

        with open("System/Extras/unos_logo.txt") as boot_sequence:
            boot_text = boot_sequence.readlines()
            for line in boot_text:
                print(line, end="")
                time.sleep(random.uniform(0, 0.10))

            print("\n")

    # def gui():
    #     pass

    # def web():
    #     pass

import json
import os
import sys
from pathlib import Path


class Config:
    def __init__(self):
        # Initial Setup
        current_directory = Path(os.getcwd())

        # Launch Configuration
        with open(f'{current_directory}\\Config\\launch_config.json') as launch_config_file:
            launch_data = json.load(launch_config_file)

            self.launch_mode = launch_data["launch_mode"]
            self.voice_recognition = launch_data["voice_recognition"]

        # UNOS Configuration
        with open(f'{current_directory}\\Config\\unos_config.json') as unos_config_file:
            unos_data = json.load(unos_config_file)

            self.unos_name = unos_data["name"]
            self.unos_version = unos_data["version"]
            self.unos_stability = unos_data["stability"]
            self.unos_codename = unos_data["codename"]
            self.unos_previous_interation = unos_data["previous_interation"]

        # Modules Configuration
        with open(f'{current_directory}\\Config\\modules_config.json') as modules_config_file:
            modules_data = json.load(modules_config_file)

            self.modules_location = modules_data["system_modules"]["location"]
            self.modules = modules_data["system_modules"]["modules"]
            self.fallback_module = modules_data["system_modules"]["fallback_module"]

        # User Configuration
        with open(f'{current_directory}\\Config\\user_config.json') as user_config_file:
            user_data = json.load(user_config_file)

            self.username = user_data["username"]
            self.date_of_birth = user_data["date_of_birth"]

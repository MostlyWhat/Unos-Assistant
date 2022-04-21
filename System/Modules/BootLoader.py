import json
import os
from pathlib import Path


class Config:
    def __init__(self):
        # Initial Setup
        current_directory = Path(os.getcwd())

        # Launch Configuration
        with open('Config/launch_config.json') as launch_config_file:
            launch_data = json.load(launch_config_file)

            self.launch_mode = launch_data["launch_mode"]
            self.voice_recognition = launch_data["voice_recognition"]
            self.dev_mode = launch_data["dev_mode"]

        # UNOS Configuration
        with open('Config/unos_config.json') as unos_config_file:
            unos_data = json.load(unos_config_file)

            self.unos_name = unos_data["name"]
            self.unos_version = unos_data["version"]
            self.unos_stability = unos_data["stability"]
            self.unos_codename = unos_data["codename"]
            self.unos_previous_interation = unos_data["previous_interation"]

        # Modules Configuration
        with open('Config/modules_config.json') as modules_config_file:
            modules_data = json.load(modules_config_file)

            self.modules_location = modules_data["system_modules"]["location"]
            self.modules = modules_data["system_modules"]["modules"]
            self.fallback_module = modules_data["system_modules"]["fallback_module"]

        # User Configuration
        with open('Config/user_config.json') as user_config_file:
            user_data = json.load(user_config_file)

            self.username = user_data["username"]
            self.date_of_birth = user_data["date_of_birth"]

        # Libaries Configuration
        with open('Config/libraries_config.json') as libraries_config_file:
            libraries_data = json.load(libraries_config_file)

            self.classes_lib = libraries_data["libraries"]["classes"]
            self.words_lib = libraries_data["libraries"]["words"]

            self.default_dataset = libraries_data["dataset"]["default"]

        # MCAS Configuration
        with open('Config/MCAS_config.json') as MCAS_config_file:
            MCAS_data = json.load(MCAS_config_file)

            self.MCAS_core1_location = MCAS_data["Cores"]["core_1"]
            self.MCAS_core2_location = MCAS_data["Cores"]["core_2"]
            self.MCAS_core3_location = MCAS_data["Cores"]["core_3"]

            with open(f'System/Cores/{self.MCAS_core1_location}') as core1_file:
                MCAS_core1_data = json.load(core1_file)

                self.MCAS_core1 = f'System/Cores/{MCAS_core1_data["info"]["name"]}/{MCAS_core1_data["info"]["filename"]}'
                self.MCAS_core1_name = MCAS_core1_data["info"]["name"]

            with open(f'System/Cores/{self.MCAS_core2_location}') as core2_file:
                MCAS_core2_data = json.load(core2_file)

                self.MCAS_core2 = f'System/Cores/{MCAS_core2_data["info"]["name"]}/{MCAS_core2_data["info"]["filename"]}'
                self.MCAS_core2_name = MCAS_core2_data["info"]["name"]

            with open(f'System/Cores/{self.MCAS_core3_location}') as core3_file:
                MCAS_core3_data = json.load(core3_file)

                self.MCAS_core3 = f'System/Cores/{MCAS_core3_data["info"]["name"]}/{MCAS_core3_data["info"]["filename"]}'
                self.MCAS_core3_name = MCAS_core3_data["info"]["name"]

        # Credentials Configuration
        with open('Config/credentials_config.json') as credentials_config_file:
            credentials_data = json.load(credentials_config_file)

            # OpenWeatherMap Api
            self.openweathermap_api = credentials_data["credentials"]["openweathermap"]["api_key"]
            self.openweathermap_city = credentials_data["credentials"]["openweathermap"]["city"]
            self.openweathermap_country = credentials_data["credentials"]["openweathermap"]["country"]
            self.openweathermap_units = credentials_data["credentials"]["openweathermap"]["units"]
            self.openweathermap_lat = credentials_data["credentials"]["openweathermap"]["lat"]
            self.openweathermap_lon = credentials_data["credentials"]["openweathermap"]["lon"]

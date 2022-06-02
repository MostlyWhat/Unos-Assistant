import json
from csv import unregister_dialect


class Config:
    def __init__(self):
        # User Config File Data Setup
        with open('Config/user_config.json') as user_config_file:
            user_data = json.load(user_config_file)
            
            # User Config
            user_config = user_data["user_config"]
            self.username = user_config["username"]
            self.date_of_birth = user_config["date_of_birth"]
            self.wakeup_commands = user_config["wakeup_commands"]
            
            # Launch Config
            launch_config = user_data["launch_config"]
            self.dev_mode = launch_config["dev_mode"]
            
            # Checks if DevMode is Enabled
            if self.dev_mode is True:
                dev_launch_config = user_data["dev_launch_config"]
                self.launch_mode = dev_launch_config["launch_mode"]
                self.voice_recognition = dev_launch_config["voice_recognition"]
                self.text_to_speech = dev_launch_config["text_to_speech"]
                
            else:
                self.launch_mode = launch_config["launch_mode"]
                self.voice_recognition = launch_config["voice_recognition"]
                self.text_to_speech = launch_config["text_to_speech"]
                
        # System Config File Data Setup
        with open('Config/system_config.json') as system_config_file:
            system_data = json.load(system_config_file)
            
            # UNOS Config
            unos_data = system_data["unos_config"]
            self.unos_name = unos_data["name"]
            self.unos_version = unos_data["version"]
            self.unos_stability = unos_data["stability"]
            self.unos_codename = unos_data["codename"]
            self.unos_previous_interation = unos_data["previous_interation"]
            
            # Providers Config
            providers_data = system_data["providers_config"]
            self.providers_recognition = providers_data["recognition"]
            self.providers_text_to_speech = providers_data["tts"]
            self.providers_audio_player = providers_data["audio_player"]
            
            # Libraries Config
            libraries_config = system_data["libraries_config"]
            libraries_data = libraries_config["libraries"]
            self.classes_lib = libraries_data["classes"]
            self.words_lib = libraries_data["words"]
            
            # Datasets Config
            datasets_data = libraries_config["datasets"]
            self.default_dataset = datasets_data["default"]
            self.mcas_dataset  = datasets_data["mcas"]
            
            # Modules Config
            modules_config = system_data["modules_config"]
            analyzers_data = modules_config["analyzers_config"]
            self.analyzers_location = analyzers_data["location"]
            self.analyzers_modules = analyzers_data["modules"]
            
            fallback_data = modules_config["fallback_config"]
            self.fallback_location = fallback_data["location"]
            self.fallback_module = fallback_data["module"]
            
            # MCAS Cores Config
            mcas_config = system_data["mcas_config"]
            self.mcas_learning = mcas_config["learning"]
            
            mcas_data = mcas_config["Cores"]
            self.mcas_core1_location = mcas_data["core_1"]
            self.mcas_core2_location = mcas_data["core_2"]
            self.mcas_core3_location = mcas_data["core_3"]

            with open(f'System/Cores/{self.mcas_core1_location}') as core1_file:
                mcas_core1_data = json.load(core1_file)

                self.mcas_core1 = f'System/Cores/{mcas_core1_data["info"]["name"]}/{mcas_core1_data["info"]["filename"]}'
                self.mcas_core1_name = mcas_core1_data["info"]["name"]

            with open(f'System/Cores/{self.mcas_core2_location}') as core2_file:
                mcas_core2_data = json.load(core2_file)

                self.mcas_core2 = f'System/Cores/{mcas_core2_data["info"]["name"]}/{mcas_core2_data["info"]["filename"]}'
                self.mcas_core2_name = mcas_core2_data["info"]["name"]

            with open(f'System/Cores/{self.mcas_core3_location}') as core3_file:
                mcas_core3_data = json.load(core3_file)

                self.mcas_core3 = f'System/Cores/{mcas_core3_data["info"]["name"]}/{mcas_core3_data["info"]["filename"]}'
                self.mcas_core3_name = mcas_core3_data["info"]["name"]
            
        # Credentials Config File Data Setup
        with open('Config/credentials_config.json') as credentials_config_file:
            credentials_config = json.load(credentials_config_file)
            credentials_data = credentials_config["credentials"]

            # OpenWeatherMap Api
            openweathermap_data = credentials_data["openweathermap"]
            self.openweathermap_api = openweathermap_data["api_key"]
            self.openweathermap_city = openweathermap_data["city"]
            self.openweathermap_country = openweathermap_data["country"]
            self.openweathermap_units = openweathermap_data["units"]
            self.openweathermap_lat = openweathermap_data["lat"]
            self.openweathermap_lon = openweathermap_data["lon"]

            # RapidAPI Api
            rapidapi_data = credentials_data["rapid_api"]
            self.rapidapi_api = rapidapi_data["api_key"]
            self.rapidapi_host = rapidapi_data["api_host"]

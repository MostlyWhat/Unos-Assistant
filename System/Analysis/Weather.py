import random

from pyowm import OWM
from pyowm.utils import config, timestamps
from System.Modules.BootLoader import Config

# Setting Up Configurations
config = Config()
owm = OWM(str(config.openweathermap_api))
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(
    f'{config.openweathermap_city}, {config.openweathermap_country}')
w = observation.weather


class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Weather"
        self.contexts = ["weather", "air", "temperature",
                         "humidity", "wind", "pressure"]

    def analyze(self, query):
        if any(context in query for context in self.contexts):
            return True

        else:
            return False

    def process(self, query):
        prefix = ["The weather is ", "The current weather is ", "Currently it is "]
        current_weather = w.detailed_status

        return random.choice(prefix) + current_weather

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
                         "humidity", "wind", "pressure", "rain", "clouds", "forecast", "cloud"]

    def analyze(self, query):
        return any(context in query for context in self.contexts)

    def process(self, query):
        # Get Initial Weather
        current_weather = w.detailed_status
        wind_speed = w.wind()["speed"]
        humidity = w.humidity
        temperature = w.temperature('celsius')["temp"]
        temperature_feel = w.temperature('celsius')["feels_like"]
        rain = w.rain
        clouds = w.clouds

        # Get Forecast but needs to be fixed due to the API key being new
        # forecaster = mgr.forecast_at_place(
        #     f'{config.openweathermap_city}, {config.openweathermap_country}', 'daily')
        # foreecast = forecaster.will_be_clear_at(timestamps.tomorrow())

        # Get Current Weather
        if "weather" in query:
            return f"The current weather is {current_weather}"

        # Get WInd Speed
        elif "wind" in query:
            return f"The wind speed is {wind_speed} m/s"

        # Get Humidity
        elif "humidity" in query:
            return f"The humidity is {humidity}%"

        # Get Temperature
        elif "temperature" in query:
            return f"The temperature is {temperature}°C with a feel like {temperature_feel}°C"

        # Get Rain
        elif "rain" in query:
            return f"The rain is {rain} mm"

        # Get Clouds
        elif "clouds" in query:
            return f"The clouds are {clouds}%"

        # Get Weather Forecast for the Next Day
        # elif "forecast" in query:
        #     return f"The weather forecast is {forecast}"

        else:
            return "Unable to process your request"

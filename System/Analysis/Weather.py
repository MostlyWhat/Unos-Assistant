
from pyowm import OWM
from pyowm.utils import config
from System.Modules.BootLoader import Config
from System.Modules.Crisis import Crisis

# Setting Up Configurations
config = Config()
crisis = Crisis()
owm = OWM(str(config.openweathermap_api))
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
try:
    observation = mgr.weather_at_place(
        f'{config.openweathermap_city}, {config.openweathermap_country}')
    w = observation.weather

except Exception as e:
    crisis.warning("Weather", "Failed to get weather data: {0}".format(e))

class Plugin:
    def __init__(self):
        self.name = "System.Analysis.Weather"
        self.contexts = ["weather", "air", "temperature",
                         "humidity", "wind", "pressure", "rain", "clouds", "forecast", "cloud"]

    def analyze(self, query):
        return any(context in query for context in self.contexts)

    @staticmethod
    def process(query):
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
        if "wind" in query:
            return f"The wind speed is {wind_speed} m/s"

        # Get Humidity
        if "humidity" in query:
            return f"The humidity is {humidity}%"

        # Get Temperature
        if "temperature" in query:
            return f"The temperature is {temperature}°C with a feel like {temperature_feel}°C"

        # Get Rain
        if "rain" in query:
            return f"The rain is {rain} mm"

        # Get Clouds
        if "clouds" in query:
            return f"The clouds are {clouds}%"

        return "Unable to process your request"

# User_Interface
from WeatherData import WeatherDataFetcher, DataParser

class UserInterface:
    def display_weather(city):
        # Function to display the basic weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = DataParser.parse_weather_data(city, data)
            print(weather_report)
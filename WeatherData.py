# WeatherData

class WeatherDataFetcher:

    def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
    # Simulated data based on city
        weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})
    
    def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(city)
        return DataParser.parse_weather_data(city, data)
    
class DataParser:
    def parse_weather_data(city, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
#        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
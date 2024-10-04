# Refactoring a Weather Forecast Application into Classes and Modules

# Weather Forecast Application Script

from WeatherData import WeatherDataFetcher, DataParser
from User_Interface import UserInterface

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = WeatherDataFetcher.get_detailed_forecast(city)
            print(forecast)
        else:
            UserInterface.display_weather(city)

if __name__ == "__main__":
    main()
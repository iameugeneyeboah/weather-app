from pyowm import OWM
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
owm = OWM(API_KEY)
mgr = owm.weather_manager()


city = input("Enter your city: ")
country = input("Enter your country code (e.g., GH for Ghana, US for USA): ")
location = f"{city},{country}"

try:
    observation = mgr.weather_at_place(location)  
    weather = observation.weather

    status = weather.detailed_status
    temperature = weather.temperature('celsius')
    wind = weather.wind()
    humidity = weather.humidity

    reporter_name = "Eugene Yeboah"
    reporting_location = "theturksonphotography, Legon"

    report = (
            f"Good day, this is {reporter_name}, reporting live from {reporting_location}.\n"
            f"Here's the latest weather update for {city.title()}, {country.upper()}:\n"
            f"Currently, we are experiencing {status} with a temperature of {temperature['temp']}°C "
            f"(feels like {temperature['feels_like']}°C). Humidity is at {humidity}%, "
            f"and wind speeds are around {wind['speed']} m/s.\n"
            f"Stay tuned to CNN for more updates.\n"
            f"you can follow me on social media at theturksonphotography"
 )

    print(report)

except FileNotFoundError:
    print("\n❌ Location not found. Please check your city and country code and try again.")
except Exception as e:
    print("\n❌ Could not retrieve weather data.")
    print(f"Reason: {e}")

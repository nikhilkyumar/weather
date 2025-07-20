import requests

# Your actual OpenWeatherMap API key
API_KEY = "549ef0f798b0e9c495cf8097c4139201"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raises HTTPError for bad responses

        data = response.json()

        city_name = data.get("name")
        country = data.get("sys", {}).get("country")
        weather = data["weather"][0]["description"].capitalize()
        temperature = round(data["main"]["temp"], 2)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n Weather in {city_name}, {country}")
        print(f" Condition  : {weather}")
        print(f" Temperature: {temperature} °C")
        print(f" Humidity   : {humidity}%")
        print(f" Wind Speed : {wind_speed} m/s")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Invalid API key. Please check your credentials.")
        elif response.status_code == 404:
            print("City not found. Please check the city name.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Get user input
city_input = input("Enter a city name: ").strip()
get_weather(city_input)

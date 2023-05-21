import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            weather_desc = data["weather"][0]["description"]

            print(f"Weather in {city}:")
            print(f"Temperature: {temperature} K")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_desc}")
        else:
            print("City not found.")
    except requests.exceptions.RequestException:
        print("An error occurred while fetching the weather data.")

# Example usage
get_weather("London")

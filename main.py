import requests

def get_weather_data(api_key, city, country_code):
    # Set up the API request URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"

    # Send the API request and get the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to get weather data: {response.text}")

    # Parse the response JSON
    data = response.json()

    # Get the relevant weather data
    weather = data["weather"][0]
    main = data["main"]
    wind = data["wind"]

    # Return the weather data as a dictionary
    return {
        "description": weather["description"],
        "icon": weather["icon"],
        "temp": main["temp"],
        "pressure": main["pressure"],
        "humidity": main["humidity"],
        "temp_min": main["temp_min"],
        "temp_max": main["temp_max"],
        "wind_speed": wind["speed"],
        "wind_deg": wind["deg"]
    }

# Example usage
api_key = input("Enter your api key:")
city = input("Enter the city: ")
country_code = input("Enter the country code: ")

weather_data = get_weather_data(api_key, city, country_code)

# Print the weather data
print(f"Description: {weather_data['description']}")
print(f"Icon: {weather_data['icon']}")
print(f"Temperature: {weather_data['temp']}")
print(f"Pressure: {weather_data['pressure']}")
print(f"Humidity: {weather_data['humidity']}")
print(f"Minimum temperature: {weather_data['temp_min']}")
print(f"Maximum temperature: {weather_data['temp_max']}")
print(f"Wind speed: {weather_data['wind_speed']}")
print(f"Wind degree: {weather_data['wind_deg']}")
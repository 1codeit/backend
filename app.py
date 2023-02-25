from flask import Flask, request, render_template
import requests
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

#Start of Azure Key Vault Code
keyVaultName = "kv-wethrer"
KVUri = f"https://kv-wethrer.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
secretName = "okey"
retrieved_secret = client.get_secret(secretName)
#end of Azure Key Vault Code

# Start of Flask Code
app = Flask(__name__)

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

        #"city": get_weather.city,
        #"country_code": get_weather.country_code,
        "icon": weather["icon"],
        "temp": main["temp"],
        "pressure": main["pressure"],
        "humidity": main["humidity"],
        "temp_min": main["temp_min"],
        "temp_max": main["temp_max"],
        "wind_speed": wind["speed"],
    }
def get_city_country_text(city, country_code):
    if request.form["cityc"] == Rolleston:
        city = Rolleston
    elif request.form["cityc"] == Auckland:
        city = Auckland
    elif request.form["cityc"] == Christchurch:
        city = Christchurch
    elif request.form["cityc"] == Wellington:
        city = Wellington


    country_code = request.form.get('country_code')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():

    # This below line is a temporary fix for the API key if it needs to be used
    # api_key = request.form["key"]
    api_key = retrieved_secret.value
    city = request.form["cityc"]
    country_code = request.form.get('country_code')

    weather_data = get_weather_data(api_key, city, country_code)

    return render_template("weather.html", weather_data=weather_data , get_city_country_text=get_city_country_text)

@app.route("/404")
def page_not_found():
    return render_template("404.html")

if __name__ == "__main__":
    app.run()
#end of Flask Code
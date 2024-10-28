#import the librays
from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

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

        "city": request.form.get('cityc'),
        "country_code": request.form.get('country_code'),    
        "icon": weather["icon"],
        "temp": main["temp"],
        "pressure": main["pressure"],
        "humidity": main["humidity"],
        "temp_min": main["temp_min"],
        "temp_max": main["temp_max"],
        "wind_speed": wind["speed"],
    }

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get_weather", methods=["POST"])
def get_weather():

    # This below line is a temporary fix for the API key if it needs to be used
    # api_key = request.form["key"]
    api_key=os.environ.get("OKEY") #("")
    city =  request.form.get('cityc')
    country_code = request.form.get('country_code')

    weather_data = get_weather_data(api_key, city, country_code)

    return render_template("weather.html", weather_data=weather_data)

@app.route("/404")
def page_not_found():
    return render_template("404.html")
@app.route("/Pages/toc/")
def Pages_Toc():
    return render_template("toc.html")
@app.route("/Pages/Privacy/")
def Privacy_pol():
    return render_template("Privacy-Policy.html")
if __name__ == "__main__":
    app.run()
#end of Flask Code
from django.shortcuts import render
import requests
import datetime
from requests.exceptions import RequestException
from decouple import config

# ===========================
# API KEY
# ===========================

OPENWEATHER_API_KEY = config("OPENWEATHER_API_KEY")


# ===========================
# HOME VIEW
# ===========================

def home(request):

    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")
    city = request.POST.get("city", "Ahmednagar")

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    # ===========================
    # GPS OR CITY SEARCH
    # ===========================

    if latitude and longitude:
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        forecast_params = params.copy()
    else:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }
        forecast_params = params.copy()

    # ===========================
    # WEATHER API CALL
    # ===========================

    try:
        response = requests.get(weather_url, params=params, timeout=10)
        data = response.json()

    except RequestException:
        return render(request, "weather/index.html", {
            "error": "⚠ Unable to connect to Weather Service."
        })

    if response.status_code != 200 or str(data.get("cod")) != "200":
        return render(request, "weather/index.html", {
            "error": "❌ City not found!"
        })

    # ===========================
    # FORECAST API CALL
    # ===========================

    forecast_list = []

    try:
        forecast_response = requests.get(
            forecast_url,
            params=forecast_params,
            timeout=10
        )
        forecast_data = forecast_response.json()

        # 5 DAY FORECAST (every 8 steps = 24 hours)
        for i in range(0, len(forecast_data["list"]), 8):
            item = forecast_data["list"][i]

            forecast_list.append({
                "date": item["dt_txt"].split(" ")[0],
                "temp": round(item["main"]["temp"]),
                "icon": item["weather"][0]["icon"],
                "desc": item["weather"][0]["main"]
            })

    except RequestException:
        forecast_list = []

    # ===========================
    # CURRENT WEATHER DATA
    # ===========================

    city = data["name"]
    weather = data["weather"][0]["main"]
    description = data["weather"][0]["description"].title()
    icon = data["weather"][0]["icon"]

    temp = round(data["main"]["temp"])
    feels_like = round(data["main"]["feels_like"])
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]

    sunrise = datetime.datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    day = datetime.date.today().strftime("%A, %d %B %Y")

    # ===========================
    # BACKGROUND
    # ===========================

    backgrounds = {
        "Clear": "https://images.unsplash.com/photo-1501973801540-537f08ccae7b?w=1600",
        "Clouds": "https://images.unsplash.com/photo-1534088568595-a066f410bcda?w=1600",
        "Rain": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?w=1600",
        "Thunderstorm": "https://images.unsplash.com/photo-1500375592092-40eb2168fd21?w=1600",
        "Snow": "https://images.unsplash.com/photo-1517299321609-52687d1bc55a?w=1600",
        "Mist": "https://images.unsplash.com/photo-1485236715568-ddc5ee6ca227?w=1600",
        "Fog": "https://images.unsplash.com/photo-1485236715568-ddc5ee6ca227?w=1600",
        "Haze": "https://images.unsplash.com/photo-1485236715568-ddc5ee6ca227?w=1600"
    }

    background = backgrounds.get(
        weather,
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=1600"
    )

    # ===========================
    # CONTEXT
    # ===========================

    context = {
        "city": city,
        "temp": temp,
        "description": description,
        "icon": icon,
        "humidity": humidity,
        "pressure": pressure,
        "wind": wind,
        "feels_like": feels_like,
        "sunrise": sunrise,
        "sunset": sunset,
        "day": day,
        "background": background,
        "forecast": forecast_list,   # 🔥 NEW FEATURE
    }

    return render(request, "weather/index.html", context)
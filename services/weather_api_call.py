import json
import requests
from django.conf import settings
from django.http import JsonResponse

from models.weather_model import WeatherModel

CURRENT_WEATHER_DATA_SERVER_DOMAIN = 'https://api.openweathermap.org123'


def currentWeatherAPICall(cityName):
    try:

        endPoint = '/data/2.5/weather?q=' + cityName + '&units=metric' + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        getCurrentWeatherDataResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        print(getCurrentWeatherDataResponse.json())

        if getCurrentWeatherDataResponse and getCurrentWeatherDataResponse.status_code == 200:
            weatherData = WeatherModel.toJsonMap(getCurrentWeatherDataResponse.json())
            return JsonResponse(weatherData, status=200)
        else:
            return JsonResponse({
                "error": "Something went wrong",
                "error_message": getCurrentWeatherDataResponse.json()['message']
            }, status=getCurrentWeatherDataResponse.status_code)

    except Exception as e:
        print(e)
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)


def historicWeatherAPCall(cityName):
    try:

        endPoint = '/data/2.5/weather?q=' + cityName + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        getCurrentWeatherDataResponse = requests.get(
            apiCallIp, headers={
                "Content-Type": "application/json",
            })

        print(getCurrentWeatherDataResponse)

    except Exception as e:
        print(e)

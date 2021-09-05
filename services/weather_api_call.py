import json
import requests
from django.conf import settings
from django.http import JsonResponse

CURRENT_WEATHER_DATA_SERVER_DOMAIN = 'https://api.openweathermap.org'


def currentWeatherAPICall(cityName):
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
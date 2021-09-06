import json
import requests
from django.conf import settings
from django.http import JsonResponse

from models.geo_model import GeoModel
from models.weather_model import WeatherModel

CURRENT_WEATHER_DATA_SERVER_DOMAIN = 'http://api.openweathermap.org'
GEOCODING_DATA_SERVER_DOMAIN = 'http://api.openweathermap.org'


def currentWeatherAPICall(cityName):
    try:
        endPoint = '/data/2.5/weather?q=' + cityName + '&units=metric' + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        getCurrentWeatherDataResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        if getCurrentWeatherDataResponse and getCurrentWeatherDataResponse.status_code == 200:
            data = getCurrentWeatherDataResponse.json()
            weatherData = WeatherModel.toJsonMap(
                clouds=data['weather'][0]['main'],
                humidity=str(data['main']['humidity']),
                pressure=str(data['main']['pressure']),
                temparature=str(data['main']['temp'])
            )
            return JsonResponse(weatherData, status=200)
        else:
            data = getCurrentWeatherDataResponse.json()
            error = "Something went wrong"
            error_code = "internal_api_error"

            if data['message'] == 'city not found':
                error = "Cannot find location '" + cityName + "'"
                error_code = "city_not_found"

            if data['message'] == 'internal_server_error':
                error = "Something went wrong"
                error_code = "internal_server_error"

            return JsonResponse({
                "error": error,
                "error_code": error_code
            }, status=getCurrentWeatherDataResponse.status_code)

    except Exception as e:
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)


def dateWeatherAPICall(lat, lng):
    try:

        endPoint = '/data/2.5/onecall?lat=' + str(lat) + '&lon=' + str(lng) + '&exclude=current,alerts' \
                   + '&units=metric' + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        dateWeatherApiCallResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        if dateWeatherApiCallResponse and dateWeatherApiCallResponse.status_code == 200:
            data = dateWeatherApiCallResponse.json()
            # weatherData = WeatherModel.toJsonMap(
            #     clouds=data['daily']['weather'][0]['main'],
            #     humidity=str(data['main']['humidity']),
            #     pressure=str(data['main']['pressure']),
            #     temparature=str(data['main']['temp_max'])
            # )
            return JsonResponse(data, status=200)

        else:
            return JsonResponse({
                "error": "Something went wrong",
                "error_message": dateWeatherApiCallResponse.json()['message']
            }, status=dateWeatherApiCallResponse.status_code)

    except Exception as e:
        print(e)
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)


def getCityGeoCoding(cityName):
    try:
        endPoint = '/geo/1.0/direct?q=' + cityName + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        # Incoming response is a list. Whether I get the data or get a blank list
        getCityGeoCodingResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        if getCityGeoCodingResponse \
                and getCityGeoCodingResponse.status_code == 200 \
                and len(getCityGeoCodingResponse.json()) > 0:
            geoCodeLatLng = GeoModel.toJsonMap(getCityGeoCodingResponse.json())
            return JsonResponse(geoCodeLatLng, status=200)

        else:
            return JsonResponse({
                "error": "Something went wrong",
                "error_message": 'city not found'
            }, status=404)

    except Exception as e:
        print(e)
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)

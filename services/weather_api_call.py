import requests
from django.conf import settings
from django.http import JsonResponse

from general import util
from models.geo_model import GeoModel
from models.weather_model import WeatherModel

CURRENT_WEATHER_DATA_SERVER_DOMAIN = 'http://api.openweathermap.org'
GEOCODING_DATA_SERVER_DOMAIN = 'http://api.openweathermap.org'


def currentWeatherAPICall(cityName):
    try:
        endPoint = '/data/2.5/weather?q=' + cityName + '&units=metric' + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        # Getting current weather data
        getCurrentWeatherDataResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        # Recieved a response properly so decoding data
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
            # means there is an error in response code. So we will destructure it and send appropriate response
            data = getCurrentWeatherDataResponse.json()
            statusCode = getCurrentWeatherDataResponse.status_code
            error = "Something went wrong"
            error_code = "internal_api_error"

            if data['message'] == 'city not found':
                error = "Cannot find location '" + cityName + "'"
                error_code = "city_not_found"

            if data['message'] == 'internal_server_error':
                error = "Something went wrong with weather service"
                error_code = "internal_api_error"

            return JsonResponse({
                "error": error,
                "error_code": error_code
            }, status=statusCode)

    except Exception as e:
        # If any error happens in parsing or the server is down, this response will be sent
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)


def dateWeatherAPICall(lat, lng, dateInfo):
    try:
        endPoint = '/data/2.5/onecall?lat=' + str(lat) + '&lon=' + str(lng) + '&exclude=current,minutely,hourly,alerts' \
                   + '&units=metric' + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        # Fetch 7 days forecast
        dateWeatherApiCallResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        if dateWeatherApiCallResponse and dateWeatherApiCallResponse.status_code == 200:
            queryDate = dateInfo['date']
            data = dateWeatherApiCallResponse.json()
            # This is daily weather forecast list data
            dailyWeatherDataList = data['daily']

            for singledailyWeatherData in dailyWeatherDataList:
                dateString = util.convertTimestampToDate(singledailyWeatherData['dt'])

                # Check if the any of the 7 days match with the query Date
                if str(dateString) == str(queryDate):
                    weatherData = WeatherModel.toJsonMap(
                        clouds=singledailyWeatherData['weather'][0]['main'],
                        humidity=str(singledailyWeatherData['humidity']),
                        pressure=str(singledailyWeatherData['pressure']),
                        temparature=str(singledailyWeatherData['temp']['day'])
                    )
                    return JsonResponse(weatherData, status=200)

            # If somehow the data is not found then send the error response
            return JsonResponse({
                "error": "You can only request up to 7 days forecast from today",
                "error_code": "future_forecast_limitation"
            }, status=400)

        else:
            # Error return in Weather service Api call
            return JsonResponse({
                "error": "Something went wrong",
                "error_code": dateWeatherApiCallResponse.json()['message']
            }, status=dateWeatherApiCallResponse.status_code)

    except Exception as e:
        # If any error happens in parsing or the server is down, this response will be sent
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)


# This api is to get Geo Coding of a particular city
def getCityGeoCoding(cityName):
    try:
        endPoint = '/geo/1.0/direct?q=' + cityName + '&appid=' + settings.WEATHER_API_KEY
        apiCallIp = CURRENT_WEATHER_DATA_SERVER_DOMAIN + endPoint

        # Incoming response is a list. I get the list data or get a blank list
        getCityGeoCodingResponse = requests.get(
            apiCallIp, timeout=5, headers={
                "Content-Type": "application/json",
            })

        # If the list has at least one data, we assume successful fetch of Lat, Lng
        if getCityGeoCodingResponse \
                and getCityGeoCodingResponse.status_code == 200 \
                and len(getCityGeoCodingResponse.json()) > 0:
            geoCodeLatLng = GeoModel.toJsonMap(getCityGeoCodingResponse.json())
            return JsonResponse(geoCodeLatLng, status=200)

        else:
            return JsonResponse({
                "error": "City not found",
                "error_code": 'city_not_found'
            }, status=404)

    except Exception as e:
        # If any error happens in parsing or the server is down, this response will be sent
        return JsonResponse({
            "error": "Something went wrong",
            "error_code": "internal_server_error"
        }, status=500)

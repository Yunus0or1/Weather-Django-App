import json
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import api_view


from services import weather_api_call

# Getting the server status
@api_view(['GET'])
def ping(request):
    return JsonResponse({"name": "weatherservice",
                         "status": "ok",
                         "version": settings.VERSION}, status=200)


@api_view(['GET'])
def getCurrentWeather(request, city):
    at = request.GET.get('at')

    # This is to get the current weather of a particular city
    if at is None:
        return weather_api_call.currentWeatherAPICall(cityName=city)

    # This is to get the current weather of a particular city in a specific date time
    if at:
        geoCodingResponse = weather_api_call.getCityGeoCoding(cityName=city)

        if geoCodingResponse.status_code == 200:
            lat = json.loads(geoCodingResponse.content)['lat']
            lng = json.loads(geoCodingResponse.content)['lng']
            return geoCodingResponse
            return weather_api_call.dateWeatherAPICall(lat, lng)

        else:
            return geoCodingResponse

    return JsonResponse({"name": "weatherservice",
                         "status": "ok",
                         "version": settings.VERSION}, status=200)

# A custom 404 json response if the url is not matched in urls.py
def custom404(request, exception=None):
    return JsonResponse({
        "error": "Something went wrong",
        "error_code": "resource not found"
    }, status=404)

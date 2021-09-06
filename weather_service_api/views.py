import json
from django.db import connection
from django.http import JsonResponse
from django.core.cache import cache
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.clickjacking import xframe_options_exempt

from services import weather_api_call


@api_view(['GET'])
def ping(request):
    return JsonResponse({"name": "weatherservice",
                         "status": "ok",
                         "version": settings.VERSION}, status=200)


@api_view(['GET'])
def getCurrentWeather(request, city):
    at = request.GET.get('at')

    if at:
        weatherData = weather_api_call.currentWeatherAPICall(cityName=city)

        return JsonResponse(weatherData, status=200)

    if at is None:
        return weather_api_call.currentWeatherAPICall(cityName=city)

    return JsonResponse({"name": "weatherservice",
                         "status": "ok",
                         "version": settings.VERSION}, status=200)

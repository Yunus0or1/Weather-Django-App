"""
weather_service URL Configuration
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import url, include
from weather_service_api import views as weather_service_api_views
from django.conf.urls import handler400, handler403, handler404, handler500

from weather_service_api.views import custom404

handler404 = custom404

urlpatterns = [
    re_path(r'^ping', weather_service_api_views.ping, name="ping"),
    re_path(r'^forecast/(?P<city>[\w|\W]+)/$', weather_service_api_views.getCurrentWeather),
]


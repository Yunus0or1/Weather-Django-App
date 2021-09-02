"""weather_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from weather_service_api import views as weather_service_api_views

urlpatterns = [
    url(r'^test/', weather_service_api_views.testCall, name="test"),
    url(r'^load_test_server/', weather_service_api_views.loadTestServer, name="load_test_server"),
    url(r'^server/', weather_service_api_views.server, name="server"),

]

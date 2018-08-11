from django.urls import path

from .views import (
	home,
	get_weather_ip,
)

urlpatterns = [
	path('', home, name='home'),
	path('get-weather-from-ip/', get_weather_ip, name='get_weather_ip'),
]
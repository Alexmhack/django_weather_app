from django.shortcuts import render
from django.http import JsonResponse

import requests
import os

def home(request):
	return render(request, "display/index.html")


def get_location_from_ip(ip_address):
	try:
		response = requests.get(f"http://ip-api.com/json/{ip_address}")
		return response.json()
	except Exception as e:
		print(e)


def get_weather_from_location(city, country_code):
	token = os.environ.get("OPEN_WEATHER_TOKEN")
	url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&units=metric&appid={token}"
	response = requests.get(url)
	return response.json()


def get_weather_ip(request):
	ip_address = request.GET.get("ip_address")
	print(ip_address)
	location = get_location_from_ip(ip_address)
	if location['status'] == "success":
		city = location.get("city")
		country_code = location.get("countryCode")
		weather_data = get_weather_from_location(city, country_code)
		description = weather_data['weather'][0]['description']
		temperature = weather_data['main']['temp']
		details = f"So you are in {city}, {country_code}. You can expect {description} with a temperature of {temperature} degres"
		data = {'weather_data': details}
		return JsonResponse(data)
	else:
		return JsonResponse(f"Failed To get location for ip_address: {ip_address}")
import os
import requests

from django.shortcuts import render
from django.http import JsonResponse


def home(request):
	return render(request, "display/index.html")


def get_location_from_ip(ip_address):
	try:
		response = requests.get(f"http://ip-api.com/json/{ip_address}")
		return response.json()
	except Exception as e:
		print(e)


def get_weather_from_location(city, country_code):
	token = open(".env").read()
	print(token)
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
		print(city, country_code)
		weather_data = get_weather_from_location(city, country_code)

		if weather_data['message'] == 'city not found':
			details = f"Failed to get weather details for your location - {city}, {country_code}"
			data = {'weather_data': details}
			return JsonResponse(data)

		print(weather_data)
		description = weather_data['weather'][0]['description']
		temperature = weather_data['main']['temp']
		details = f"So you are in {city}, {country_code}. You can expect {description} with a temperature of {temperature} degrees"
		data = {'weather_data': details}
		return JsonResponse(data)
	else:
		details = f"Failed to get your location IP: {ip_address}"
		data = {'weather_data': details}
		return JsonResponse(data)
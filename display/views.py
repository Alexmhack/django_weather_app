from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
	return render(request, "display/index.html")


def get_location_from_ip(ip_address):
	try:
		response = requests.get("http://ip-api.com/json/{}").format(ip_addresss)
		return response.json()
	except Exception as e:
		print(e)


def get_weather_ip(request):
	ip_address = request.GET.get("ip_address")
	print(ip_address)
	location = get_location_from_ip(ip_address)
	city = location.get("city")
	country_code = location.get("countryCode")
	details = "So you are in {}, {}".format(city, country_code)
	data = {'weather_data': details}
	return JsonResponse(data)
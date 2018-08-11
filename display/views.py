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
	print("IP ADDRESS: " + request.GET.get("ip_address"))
	data = {'weather_data': 20}
	return JsonResponse(data)
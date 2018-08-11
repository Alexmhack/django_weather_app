from django.shortcuts import render
from django.http import JsonResponse

def home(request):
	return render(request, "display/index.html")


def get_weather_ip(request):
	print("IP ADDRESS: " + request.GET.get("ip_address"))
	data = {'weather_data': 20}
	return JsonResponse(data)
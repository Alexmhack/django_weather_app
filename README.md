# django_weather_app
Displaying the weather for the user using his current location

# INSTALLATIONS
1. Django

# CONFIGURING
Create a new django project inside the root folder using

django-admin startproject weather .

Note the dot after the name of the project.

Create two folders > templates and static in the main folder like the tree below


	...
-	manage.py 
+ 	templates
	- 	base.html
	+ 	weather
		- 	index.html
+ static
	+ 	css
		- 	style.css


We will be getting the ip address of the user using the api from ipify, this api supports many 
languages including python, but we will use the javascript api for our purpose.

Just place this script in the head of our base.html file

<script>
	function get_ip(json) {
		alert("Your IP Address is: " + json.ip);
	}	
</script>

<script src="https://api.ipify.org?format=jsonp&callback=get_ip"></script>

NOTE: the function name and our callback from the ipify url are the same, this connects our function
with the json the api will send on request.

Run the first migrate and createsuperuser.

# Django App
Create a new django app display for displaying the current location weather for a particular user
by fetching his ip address, but first we need to make a fake data repsonder for starters.

Create a new view function named get_weather_ip

NOTE: Django by default sends a request object with every request made to a view from its url, so 
here we are going to use that request object to get the ip_address from the request, this ip_address 
is the one that the ipify api is sending us as json,

```
request.GET.get("ip_address")
```

We will print this ip_address from our view function into the terminal and just create a fake json
data using python dict

```
data = {'weather_data': 20}
```

this fake data says the current temperature is 20 degree Celcius

Next we need to send this data again so we will use the JsonResponse from django.http and return this
response from our view

```
return JsonResponse(data)
```

Now open the localhost with ?ip_address=123 at last of our view url

http://127.0.0.1:8000/get-weather-from-ip/?ip_address=123
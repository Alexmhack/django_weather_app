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


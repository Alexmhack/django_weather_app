function get_ip(json) {
	$.ajax({
	    url: {% url 'get_weather_ip' %},
	    data: {'ip_address': json.ip},
	    dataType: 'json',
	    success: function(data) {
	        $("#weatherdata").html(data.weather_data)
	    }
	})
}
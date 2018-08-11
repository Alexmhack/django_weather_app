from django.urls import path

from .views import (
	home,
)

urlpatterns = [
	path('', views.home, name='home'),
]
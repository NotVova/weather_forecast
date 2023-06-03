from django.urls import path
from .views import weather_app

urlpatterns = [
    path('', weather_app, name='weather_app')
]

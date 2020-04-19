from django.urls import path

from .views import AddTemperatureView

app_name = 'temp_monitor'

urlpatterns = [
    path('add_temp/', AddTemperatureView.as_view(), name='add_temp'),
]

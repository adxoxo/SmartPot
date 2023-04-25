from django.urls import path
from .views import TemperatureHumidityView

urlpatterns = [
    path('temphumid/', TemperatureHumidityView.as_view({
        'get':'temphumidlist',
        'post':'temphumidread'
    }))
]
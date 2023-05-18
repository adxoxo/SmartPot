from django.urls import path
from .views import TemperatureHumidityView, LightSensorView, SoilMoistureView

urlpatterns = [
    path('temphumid/', TemperatureHumidityView.as_view({
        'get':'temphumidlist',
        'post':'temphumidread'
    })),
    path('light', LightSensorView.as_view({
        'get': 'lightlist',
        'post': 'lightread'
    })),
    path('soil', SoilMoistureView.as_view({
        'get': 'moisturelist',
        'post': 'moistureread'
    }))
]
from django.contrib import admin
from .models import TempHumid, Light, SoilMoisture, SmartPot
# Register your models here.
admin.site.register(TempHumid)
admin.site.register(Light)
admin.site.register(SoilMoisture)
admin.site.register(SmartPot)
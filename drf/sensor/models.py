from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TempHumid(models.Model):
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Light(models.Model):
    light = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
class PlantStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surrounding = models.ForeignKey(TempHumid, on_delete=models.CASCADE)
    lux = models.ForeignKey(Light, on_delete=models.CASCADE)
    
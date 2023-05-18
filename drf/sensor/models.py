from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class SmartPot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

class TempHumid(models.Model):
    pot = models.ForeignKey(SmartPot, on_delete=models.CASCADE, null=True)
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Light(models.Model):
    pot = models.ForeignKey(SmartPot, on_delete=models.CASCADE, null=True)
    light = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class SoilMoisture(models.Model):
    pot = models.ForeignKey(SmartPot, on_delete=models.CASCADE, null=True)
    voltage = models.IntegerField(default=0)
    moisture = models.IntegerField(default=0)
    
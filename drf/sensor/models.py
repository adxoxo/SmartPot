from django.db import models

# Create your models here.
class TempHumid(models.Model):
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
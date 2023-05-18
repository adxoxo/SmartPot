from .models import TempHumid, Light, SoilMoisture
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class TempHumidSerializer(ModelSerializer):
    class Meta:
        model = TempHumid
        fields = '__all__'

class LightSerializer(ModelSerializer):
    class Meta:
        model = Light
        fields = '__all__'

class MoistureSerializer(ModelSerializer):
    class Meta:
        model = SoilMoisture
        fields = '__all__'
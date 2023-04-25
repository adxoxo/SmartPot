from .models import TempHumid
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class TempHumidSerializer(ModelSerializer):
    class Meta:
        model = TempHumid
        fields = '__all__'
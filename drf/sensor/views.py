from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .serializers import TempHumidSerializer, LightSerializer, MoistureSerializer, AveragePercentSerializer
from .models import TempHumid, SoilMoisture

class TemperatureHumidityView(ViewSet):
    
    def temphumidlist(self, request):
        data = TempHumid.objects.all()

        total_sum = sum(obj.temp for obj in data)
        total_count = data.count()  
        average_value = total_sum / total_count if total_count > 0 else 0
        average_percentage = (average_value / 100)
        average_actualpercentage = round((average_value / 100) * 100, 2)


        serializer_average = AveragePercentSerializer({
            'average_percent':average_percentage,
            'average_actualpercent':average_actualpercentage
        })
        serializer_all = TempHumidSerializer(data, many=True)
        
        response_data = {
            'average':serializer_average.data,
            'all':serializer_all.data,
        }

        return Response(response_data, status=200)
    
    #sensor sends POST data to DRF
    @csrf_exempt
    def temphumidread(self, request):
        serializer = TempHumidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)

class LightSensorView(ViewSet):

    def lightlist(self, request):
        data = Light.objects.all()
        serializer = LightSerializer(data, many=True)

        return Response(serializer.data, status=200)

    def lightread(self, request):
        serializer = LightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)

class SoilMoistureView(ViewSet):

    def moisturelist(self, request):
        data = SoilMoisture.objects.all()
        serializer = MoistureSerializer(data, many=True)

        return Response(serializer.data, status=200)

    def moistureread(self, request):
        serializer = MoistureSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .serializers import TempHumidSerializer
from .models import TempHumid

class TemperatureHumidityView(ViewSet):
    
    def temphumidlist(self, request):
        data = TempHumid.objects.all()
        serializer = TempHumidSerializer(data, many=True)

        return Response(serializer.data, status=200)
    
    #sensor sends POST data to DRF
    @csrf_exempt
    def temphumidread(self, request):
        serializer = TempHumidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=400)
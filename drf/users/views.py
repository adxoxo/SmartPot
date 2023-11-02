from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import User
from .serializers import SignUpSerializer

class SignUpView(ViewSet):
    
    def create(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user = User(
                first_name = validated_data.get('first_name'),
                last_name = validated_data.get('last_name'),
                email = validated_data.get('email')
            )
            user.set_password(validated_data.get('password'))
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors)
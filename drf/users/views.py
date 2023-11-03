from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import SignUpSerializer, LoginSerializer
from django.contrib.auth import authenticate

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

class LoginView(ViewSet):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            email = validated_data['email']
            password = validated_data['password']
            user = authenticate(request, email=email, password=password)
            if User is not None:
                token = Token.objects.get(user=user)
                response = {
                    "message": "success",
                    "data":{
                        "Token": token.key
                    }
                }
            return Response(response)
        else:
            respones = {
                "data": serializer.errors
            }
        return Response(response)

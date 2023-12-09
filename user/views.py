from django.shortcuts import render
from .serializers import CustomUserSerializer,CustomUserTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CustomUserSerializer
from django.contrib.auth.models import AbstractUser
from django.shortcuts import get_object_or_404
from .models import CustomUser
@api_view(['POST'])
def register_user(request):
    if request.method=='POST':
        serializer=CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomUSerToken(APIView):
    def post(self,request):
        serializer=CustomUserTokenSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            user=CustomUser.objects.filter(username=username).first()
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
           


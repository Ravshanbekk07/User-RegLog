from django.shortcuts import render
from .serializers import CustomUserSerializer,CustomUserTokenSerializer,LoginSerializer
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
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import logout



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
            user=get_object_or_404(CustomUser,username=username)
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                refresh=RefreshToken.for_user(user)
                return Response({ 'refresh': str(refresh),'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            logout(request)
            return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Unable to logout'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

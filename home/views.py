from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .serializers import RegisterSerializer

class OpenView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message':'Anyone can see this'})
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message':f'Hello{request.user.username}!'})
    
class RegisterAPI(APIView):
    def post(self,request):
        _data = request.data
        serializer = RegisterSerializer(data=_data)

        if not serializer.is_valid():
            return Response({'message':serializer.errors},status=status.HTTP_404_NOT_FOUND)

        serializer.save()
        return Response({'message':'user created'},status=status.HTTP_201_CREATED)
    

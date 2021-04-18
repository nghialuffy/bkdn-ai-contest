from bson import json_util
from rest_framework import permissions, viewsets, status, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models import Contest
from api.serializers.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from api.serializers.ContestSerializer import ContestSerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    
class ContestList(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    permissions = [permissions.AllowAny]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ContestSerializer(queryset, many=True)
        return Response(serializer.data)

class ContestInfo(generics.GenericAPIView):
    queryset = Contest.objects
    serializer_class = ContestSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("Contest is deleted successful")

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Contest is updated successful'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Contest is updated unsuccessful'
        }, status=status.HTTP_400_BAD_REQUEST)
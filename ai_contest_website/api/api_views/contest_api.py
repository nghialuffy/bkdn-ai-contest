from bson import json_util
from rest_framework import permissions, viewsets, status, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models import Contest, User
from api.serializers.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from api.serializers.ContestSerializer import ContestSerializer

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    
class ContestList(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ContestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # user = User.objects.get(pk=request.user.id)
        # request.data["created_user"] = {'id':request.user.id}
        print(request.user.id)
        user = User.objects.filter(pk=request.user.id).first()
        # request.data['created_user'] = user
        print(request.data)
        temp_request = request.data.copy()
        temp_request['created_user'] = request.user.id
        print(temp_request)
        serializer = ContestSerializer(data=temp_request)
        if serializer.is_valid():
            print('valided')
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class ContestInfo(generics.GenericAPIView):
    queryset = Contest.objects
    serializer_class = ContestSerializer

    def get(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        operator = obj.delete()
        data = {}
        if operator:
            data["success"] = "Delete contest successful"
        else:
            data["failure"] = "Delete contest failed"
        return Response(data=data)

    def put(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ContestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Contest is updated successful'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Contest is updated failed'
        }, status=status.HTTP_400_BAD_REQUEST)

class AttendedContest(generics.GenericAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    def get(self, request, *args, **kwargs):
        id = self.kwargs['id']
        print("id: ", id)
        queryset = self.get_queryset()
        # queryset = queryset.filter(title='BKDN AI')
        # testList = ["BKDN AI","bkdnContest 1"]
        queryset = queryset.filter(contestants=id)
        # queryset = queryset.filter(username__in = contestList)
        # queryset = queryset.filter(contestants=username)
        serializer = ContestSerializer(queryset, many=True)
        return Response(serializer.data)
from bson import json_util
from rest_framework import permissions, viewsets, status, views, generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models import Problem
from api.serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from api.serializers.ProblemSerializer import ProblemSerializer 
from rest_framework.parsers import MultiPartParser, FormParser
def index(request):
    list_problem = Problem.objects.all()

class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        if request.GET.get('contest_id'):
            contest_id = request.GET.get('contest_id', '')
            queryset = queryset.filter(contest_id=contest_id)
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)

class ProblemInfo(generics.GenericAPIView):
    queryset = Problem.objects
    serializer_class = ProblemSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status = status.HTTP_404_NOT_FOUND)
        data = {}
        if operator:
            data["message"] = "Delete problem successful"
        else:
            data["message"] = "Delete problem failed"
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        obj = Problem(code_test=request.FILES)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProblemUpload(views.APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        Response(data={"OK":'OK'}, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        print(request.data)
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
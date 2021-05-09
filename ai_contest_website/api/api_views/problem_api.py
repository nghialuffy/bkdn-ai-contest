from bson import json_util
from rest_framework import permissions, viewsets, status, views, generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models import Problem, Contest, Language
from api.serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from api.serializers.ProblemSerializer import ProblemSerializer 
from rest_framework.parsers import MultiPartParser, FormParser
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

    def create(self, request, *args, **kwargs):
        # Get contest object
        contest = Contest.objects.filter(pk=request.data['contest']).first()

        # Get language object
        languages = request.data['languages'].split(', ')
        language_objects = list()
        for item in request.data['languages'].split(', '):
            language_objects.append(Language.objects.filter(pk=item).first())
        print('******************************')
        print(language_objects)

        temp_queryset = request.data.copy()
        temp_queryset['languages'] = languages
        print(temp_queryset)
        serializer = ProblemSerializer(data=temp_queryset)
        if serializer.is_valid():
            print('*******************valided*************')
            serializer.validated_data['contest'] = contest
            serializer.validated_data['languages'] = language_objects
            print(serializer.validated_data)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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
        operator = obj.delete()
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
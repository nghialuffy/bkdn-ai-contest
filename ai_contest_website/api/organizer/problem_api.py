from bson import json_util
from rest_framework import permissions, viewsets, status, views, generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models import Problem, Contest, Language
from api.serializers.UserSerializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from api.serializers.ProblemSerializer import ProblemSerializer, CreateProblemSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class OrganizerProblemList(generics.ListCreateAPIView):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()
    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        contest_id = kwargs.get('contest_id', '')
        print(contest_id)
        queryset = Problem.objects.filter(contest_id=contest_id)
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)

    # Create a problem
    def create(self, request, *args, **kwargs):
        # Get contest object
        try:
            contest = Contest.objects.filter(pk=request.data['contest']).first()
        except Exception:
            data = {'error': 'Can not find contest'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        # Get language object
        languages = request.data['languages'].split(', ')
        temp_queryset = request.data.copy()
        serializer = CreateProblemSerializer(data=temp_queryset)
        if serializer.is_valid():
            serializer.validated_data['contest'] = contest
            serializer.save()
            problem = Problem.objects.get(pk=serializer.data['_id'])
            try:
                for item in request.data['languages'].split(', '):
                    problem.languages.add(Language.objects.filter(pk=item).first())
            except Exception:
                data = {'error': 'Can not find language'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)
            problem.save()
            # problem.update()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizerProblemInfo(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProblemSerializer

    def get(self, request, *args, **kwargs):
        problem_id = kwargs.get('problem_id')
        try:
            problem = Problem.objects.get(pk=problem_id)
            print(problem)
            serializer = self.get_serializer(problem)
            return Response(serializer.data)
        except Exception:
            data = {'error': 'Can not find problem'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        problem_id = kwargs.get('problem_id')
        obj = Problem.objects.get(pk=problem_id)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from bson import json_util
from rest_framework import permissions, viewsets, status, views, generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Result, Problem, Contest, User, Language
from api.serializers.ResultSerializer import ResultSerializer, ResultSubmitSerializer

class ResultList(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ResultSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        # get User
        user = User.objects.filter(pk=request.user.id).first()
        problem = Problem.objects.filter(_id=request.data['problem_id']).first()
        print(request.user.id)
        print(request.data)
        print(user)
        print(problem)
        temp_queryset = request.data.copy()
        temp_queryset['created_user'] = user
        temp_queryset['problem_id'] = request.data['problem_id']
        print(temp_queryset)
        serializer = ResultSubmitSerializer(data=temp_queryset)
        if serializer.is_valid():
            language = Language.objects.filter(_id=request.data['language_id']).first()
            if language is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data['language'] = language
            serializer.validated_data['created_user'] = user
            serializer.validated_data['problem'] = problem
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultInfo(generics.GenericAPIView):
    queryset = Result.objects
    serializer_class = ResultSerializer

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
            data["message"] = "Delete result successful"
        else:
            data["message"] = "Delete result failed"
        return Response(data=data)

    # def post(self, request, *args, **kwargs):
    #     obj = Result()
    #     serializer = self.get_serializer(obj, data=request.data, partial=True)
    #     lookup_field = 'pk'
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status = status.HTTP_201_CREATE)
    #     else:
    #         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

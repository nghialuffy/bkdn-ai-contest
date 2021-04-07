from bson import json_util
from rest_framework import permissions, viewsets, status, views
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from api.models.User import User
from api.serializers.UserSerializer import UserSerializer
from rest_framework.renderers import JSONRenderer

# @api_view(['GET'])
# def get_user(request):

#     # TODO Only for testing purposes!
#     str = json_util.dumps(query)
#     campaigns = json_util.loads(str)
#     return Response(campaigns)
def index(request):
    list_user = list(User.objects.all())
    serializer = serializers.serialize('json', list_user)
    print(serializer)
    return JsonResponse({"result":serializer})
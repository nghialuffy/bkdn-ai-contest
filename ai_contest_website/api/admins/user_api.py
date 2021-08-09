from django.contrib.auth.hashers import make_password, get_hasher
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from api.permissions.permissions import IsSSOAdmin
from api.models import User, Contest
from api.serializers.UserSerializer import UserSerializer, RegisterUserSerializer, UserLoginSerializer, \
    UserLoginRespSerializer
from api.serializers import ContestAttendedSerializer
from api.serializers import UserContestAttendedSerializer
import copy


class AdminUserList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    # permission_classes = [IsSSOAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class AdminUserInfo(generics.GenericAPIView):
    queryset = User.objects
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response({"detail": "User is deleted successful"})


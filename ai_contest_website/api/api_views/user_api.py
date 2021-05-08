from django.contrib.auth.hashers import make_password, get_hasher
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils import json
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from api.permissions.permissions import IsSSOAdmin
from api.models import User, Contest
from api.serializers.UserSerializer import UserSerializer, RegisterUserSerializer, UserLoginSerializer,UserLoginRespSerializer
from api.serializers import ContestAttendedSerializer

class UserList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsSSOAdmin]
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

class UserInfo(generics.GenericAPIView):
    queryset = User.objects
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("Language is deleted successful")



class UserRegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.GenericAPIView):
    permissions = [permissions.AllowAny]
    serializer_class = UserLoginRespSerializer
    query_set = User.objects

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = self.authenticate(
                request,
                username = serializer.data['username'],
                password = serializer.data['password']
            )
            print(user)
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                }
                return Response(data, status=status.HTTP_200_OK)

            return Response({
                'error_message': 'Username or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)

    def authenticate(self, request, username=None, password=None):
        user = User.objects.get(username=username)
        if user != None:
            hash_password = user.password
            pwd_valid = check_password(password, hash_password)
            if pwd_valid:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    # Create a new user. There's no need to set a password
                    # because only the password from settings.py is checked.
                    user = User(username=username)
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                
                print(user)
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class UserListAttendedContest(generics.GenericAPIView):
    # serializer_class = UserContestAttendedSerializer
    queryset = User.objects
    def get(self, req, *args, **kwargs):
        obj = self.get_object()
        print(obj)
        data = obj.attended_contest.all()
        ser = ContestAttendedSerializer(data, many=True)
        return Response(ser.data)


class JoinContest(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        obj = request.user
        contest_id = request.data.get('contest_id')
        print(contest_id)

        obj = User.objects.filter(_id=obj.id).first()
        contest = Contest.objects.filter(_id=contest_id).first()
        obj.attended_contest.add(contest)
        return Response('Ok')
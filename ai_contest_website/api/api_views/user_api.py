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
        return Response({"detail": "User is deleted successful"})


class UserRegisterView(generics.GenericAPIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
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
                username=serializer.data['username'],
                password=serializer.data['password']
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
        try:
            user = User.objects.get(username=username)
        except Exception as exc:
            return None
        hash_password = user.password
        pwd_valid = check_password(password, hash_password)
        if pwd_valid:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# TODO: Delete this because migrated it to user folder 
class UserListAttendedContest(generics.GenericAPIView):
    # serializer_class = UserContestAttendedSerializer
    queryset = User.objects

    def get(self, req, *args, **kwargs):
        obj = self.get_object()
        data = obj.attended_contests.all()
        ser = ContestAttendedSerializer(data, many=True)
        return Response(ser.data)


# TODO: Delete this because migrated it to user folder
class JoinContest(generics.GenericAPIView):
    serializer_class = UserContestAttendedSerializer

    def post(self, request, *args, **kwargs):
        obj = request.user
        contest_id = request.data.get('contest_id')

        obj = User.objects.get(_id=obj.id)
        contest = Contest.objects.get(_id=contest_id)

        if contest is not None:
            new_obj = copy.deepcopy(obj)
            new_obj.attended_contests.add(contest)
            ser = self.get_serializer(new_obj, data=obj.__dict__)
            if ser.is_valid():
                contest.attended_contestants.add(new_obj)
                ser.save()
                return Response(ser.data)
            return Response({
                'error_messages': ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'error_messages': 'Contest not found!'
        }, status=status.HTTP_400_BAD_REQUEST)

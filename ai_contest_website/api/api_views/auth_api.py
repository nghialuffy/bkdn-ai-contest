from rest_framework import generics, status
from django.contrib.auth.hashers import make_password, get_hasher
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from api.models import User
from api.serializers.UserSerializer import UserLoginSerializer, UserLoginRespSerializer
from api.serializers.UserSerializer import UserAdminPASerializer
from api.serializers.UserSerializer import UserOrganizerPASerializer


class UserInfoLogin(generics.GenericAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserLoginRespSerializer

    def get(self, request, *args, **kwargs):
        userInfo = User.objects.get(_id=request.user.id)
        s_userInfo = self.get_serializer(userInfo)
        return Response(s_userInfo.data)


class AdminPermissionAuthorization(generics.UpdateAPIView):
    serializer_class = UserAdminPASerializer

    def update(self, request, *args, **kwargs):
        if 'user_id' not in request.data \
                or 'is_organizer' not in request.data:
            return Response({
                "error_messages": 'Bad request'
            }, status=status.HTTP_400_BAD_REQUEST)
        user_id = request.data['user_id']
        is_admin = request.data['is_admin']
        user = User.objects.get(_id=user_id)
        user.is_admin = int(is_admin) == 1
        ser = self.get_serializer(user, data=user.__dict__)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
            'error_message': ser.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class OrganizerPermissionAuthorization(generics.UpdateAPIView):
    serializer_class = UserOrganizerPASerializer

    def update(self, request, *args, **kwargs):
        if 'user_id' not in request.data \
                or 'is_organizer' not in request.data:
            return Response({
                "error_messages": 'Bad request'
            }, status=status.HTTP_400_BAD_REQUEST)

        user_id = request.data['user_id']
        is_organizer = request.data['is_organizer']
        user = User.objects.get(_id=user_id)
        user.is_organizer = int(is_organizer) == 1
        ser = self.get_serializer(user, data=user.__dict__)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response({
            'error_message': ser.errors
        }, status=status.HTTP_400_BAD_REQUEST)



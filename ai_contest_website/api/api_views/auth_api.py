from rest_framework import generics
from django.contrib.auth.hashers import make_password, get_hasher
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from api.models import User
from api.serializers.UserSerializer import UserLoginSerializer, UserLoginRespSerializer

class UserInfoLogin(generics.GenericAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserLoginRespSerializer
    def get(self, request, *args, **kwargs):
        userInfo = User.objects.get(_id=request.user.id)
        s_userInfo = self.get_serializer(userInfo)
        return Response(s_userInfo.data)
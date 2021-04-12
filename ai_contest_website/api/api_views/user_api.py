from rest_framework import generics, permissions
from rest_framework.response import Response
from api.models import User
from api.serializers.UserSerializer import UserSerializer,RegisterUserSeriallizer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions = [permissions.AllowAny]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
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
class RegisterUser(generics.GenericAPIView):
    queryset = User.objects
    serializer_class = RegisterUserSeriallizer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("Language is deleted successful")

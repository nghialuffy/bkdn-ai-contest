from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from api.models import Language, User
from api.permissions.permissions import IsSSOAdmin, IsOrganizerOrReadOnly, IsAdminOrReadOnly
from .serializers.language_serializers import AdminLanguageSerializer
from bson import ObjectId


class AdminLanguageList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Language.objects.all()
    serializer_class = AdminLanguageSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AdminLanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class AdminLanguageInfo(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Language.objects
    serializer_class = AdminLanguageSerializer

    def get(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # user = JWTAuthentication.get_user(request)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
        

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        operator = obj.delete()
        data = {}
        if operator:
            data["success"] = "Delete language successful"
        else:
            data["failure"] = "Delete language failed"
        return Response(data=data)




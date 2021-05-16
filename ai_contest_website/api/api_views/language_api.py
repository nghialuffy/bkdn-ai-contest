from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from api.models import Language, User
from api.permissions.permissions import IsSSOAdmin, IsOrganizerOrReadOnly, IsAdminOrReadOnly
from api.serializers.LanguageSerializer import LanguageSerializer
from bson import ObjectId

class LanguageList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        # TokenUser.
        print('***********************')
        print(request.user.id)
        user = User.objects.get(pk=request.user.id)
        print(user.username)
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguageInfo(generics.GenericAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Language.objects
    serializer_class = LanguageSerializer

    def get(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = JWTAuthentication.get_user(request)
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

    def put(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Exception as exc:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Update language successful"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
    


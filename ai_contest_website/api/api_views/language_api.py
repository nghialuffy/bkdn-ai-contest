from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from api.models import Language
from api.permissions.permissions import IsSSOAdmin
from api.serializers.LanguageSerializer import LanguageSerializer

class LanguageList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsSSOAdmin]
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguageInfo(generics.GenericAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Language.objects
    serializer_class = LanguageSerializer

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("Language is deleted successful")

    def put(self, request, *args, **kwargs):
        print(request)
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        lookup_field = 'pk'
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Language updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
    


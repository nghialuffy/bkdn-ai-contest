from rest_framework import generics
from rest_framework.response import Response

from api.models import Language
from api.serializers.LanguageSerializer import LanguageSerializer

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # print(queryset)
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguageInfo(generics.GenericAPIView):
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
    


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication, JWTAuthentication
from api.models import Language, User
from .serializers.language_serializers import OrganizerLanguageSerializer
from bson import ObjectId


class OrganizerLanguageList(generics.ListCreateAPIView):
    authentication_classes = [JWTTokenUserAuthentication]
    queryset = Language.objects.all()
    serializer_class = OrganizerLanguageSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = OrganizerLanguageSerializer(queryset, many=True)
        return Response(serializer.data)


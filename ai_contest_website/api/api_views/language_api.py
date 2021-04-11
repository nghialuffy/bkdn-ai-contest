from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Language
from api.serializers.LanguageSerializer import LanguageSerializer
@api_view(['GET', 'POST'])
def index(request):
    print('Language request')
    if request.method == 'GET':        
        list_language = Language.objects.all()
        serializer = LanguageSerializer(list_language, many=True)
        data = {'data': serializer.data}
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        print(request)
        language_serializer = LanguageSerializer(data=request.data)
        data = {}

        if language_serializer.is_valid():
            language_serializer.save()
            print(Response(language_serializer.data, status=status.HTTP_201_CREATED))
            return Response(language_serializer.data, status=status.HTTP_201_CREATED)

        return Response(language_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_item(request):
    if request.method == 'GET':        
        list_language = Language.objects.all()
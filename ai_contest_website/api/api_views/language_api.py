from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Language
from api.serializers.LanguageSerializer import LanguageSerializer
@api_view(['GET'])
def list_all(request):
    if request.method == 'GET':        
        list_language = Language.objects.all()
        serializer = LanguageSerializer(list_language, many=True)
        data = {'data': serializer.data}
        return JsonResponse(data, safe=False)

@api_view(['POST'])
def add_language(request):
    if request.method == 'POST':
        language = Language.objects.get(name='python') 
        language_serializer = LanguageSerializer(data=language)
        data = {}

        if language_serializer.is_valid():
            data['response'] = "Add language successfully!"
            data['name'] = language.name
            data['path'] = language.path
        else:
            data = language_serializer.errors
        
        print(JsonResponse(data, safe=False))
        return JsonResponse(data)
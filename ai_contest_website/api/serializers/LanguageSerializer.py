from rest_framework import serializers
from api.models import Language
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'created', 'path')
    
    
    def save(self, *args, **kwargs):
        language = super(Language, self).save(**kwargs)
        return language

list_language = Language.objects.all()
serializer_class = LanguageSerializer(list_language, many=True)
print(JSONRenderer().render(serializer_class.data))
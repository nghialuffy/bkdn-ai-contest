from rest_meets_djongo.serializers import DjongoModelSerializer
from api.models import HtmlDocument
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
class HtmlDocumentSerializer(DjongoModelSerializer):
    class Meta:
        model = HtmlDocument
        fields = ('_id', 'name', 'html_content')
    
    def update(self, instance, validated_data):
        instance._id = validated_data.get('_id', instance._id)
        instance.name = validated_data.get('name', instance.name)
        instance.html_content = validated_data.get('html_content', instance.html_content)
        instance.save()
        return instance
from rest_meets_djongo.serializers import DjongoModelSerializer
from api.models import Language
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
class LanguageSerializer(DjongoModelSerializer):
    class Meta:
        model = Language
        fields = ('_id', 'name', 'created', 'path')
    
    def create(self, validated_data):
        language = Language.objects.create(**validated_data)
        return language

    def update(self, instance, validated_data):
        instance._id = validated_data.get('_id', instance._id)
        instance.name = validated_data.get('name', instance.name)
        instance.path = validated_data.get('path', instance.path)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
    
    # def save(self, **kwargs):
    #     super(Language, self).save(**kwargs)

    def validate(self, data):
        validated_data = data
        return validated_data
        # if data['start'] > data['finish']:
        #     raise serializers.ValidationError("finish must occur after start")
        # return data
    # def validated_data(self, value)
# print("================")
# list_language = Language.objects.all()
# serializer_class = LanguageSerializer(list_language, many=True)
# print(JSONRenderer().render(serializer_class.data))
# l = Language(name='c++')
# # l.save()
# print(list(Language.objects.all()))
# print("================")



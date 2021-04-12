from rest_framework import serializers
from api.models import Contest
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from api.serializers.UserSerializer import UserSerializer
from api.serializers.LanguageSerializer import LanguageSerializer
class ContestSerializer(serializers.ModelSerializer):
    created_user = UserSerializer()
    language = LanguageSerializer(many=True)
    constestants = UserSerializer(manuy=True)
    class Meta:
        model = Contest
        fields = ('title', 'created_user', 'created', 'constestants', 'language', 'time_start', 'time_end')

    def create(self, validated_data):
        contest = Contest.objects.create(**validated_data)
        return contest

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.created_user = validated_data.get('created_user', instance.created_user)
        instance.created = validated_data.get('created', instance.created)
        instance.constestants = validated_data.get('constestants', instance.constestants)
        instance.language = validated_data.get('language', instance.language)
        instance.time_start = validated_data.get('time_start', instance.time_start)
        instance.time_end = validated_data.get('time_end', instance.time_end)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return data

# contest = Contest(title="Nghialuffy")
# serializer_class = ContestSerializer(contest)
# print(JSONRenderer().render(serializer_class.data))
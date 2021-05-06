from rest_meets_djongo.serializers import DjongoModelSerializer
from djongo import models
from api.models import Contest
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from api.serializers.UserSerializer import UserIdSerializer
from api.serializers.LanguageSerializer import LanguageSerializer
from rest_framework import serializers


class ContestSerializer(DjongoModelSerializer):
    created_user = serializers.StringRelatedField()
    # language = LanguageSerializer(many=True)
    # contestants = UserIdSerializer(many=True)
    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created' , 'created_user', 'time_start', 'time_end')

    def create(self, validated_data):
        contest = Contest.objects.create(**validated_data)
        return contest

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.created_user = validated_data.get('created_user', instance.created_user)
        instance.created = validated_data.get('created', instance.created)
        # instance.contestants = validated_data.get('contestants', instance.contestants)
        # instance.language = validated_data.get('language', instance.language)
        instance.time_start = validated_data.get('time_start', instance.time_start)
        instance.time_end = validated_data.get('time_end', instance.time_end)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return validated_data
class ContestIdSerializer(DjongoModelSerializer):
    class Meta:
        model = Contest
        fields = ['_id']

    def create(self, validated_data):
        contest = Contest.objects.create(**validated_data)
        return contest

    def validate(self, data):
        validated_data = data
        # validated_data['created_user'] = JSONFIeld.to_internal_value(data['created_user'])
        return data
# contest = Contest(title='bkdnContest 1')
# contest.save()
# serializer_class = ContestSerializer(contest)
# print(JSONRenderer().render(serializer_class.data))
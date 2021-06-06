import json

from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from djongo import models
from api.models import Contest
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from api.serializers.UserSerializer import UserIdSerializer
from api.serializers.UserSerializer import UserListContestSerializer
from api.serializers.LanguageSerializer import LanguageNameSerializer
from rest_framework import serializers

# from bson import ObjectId
# from bson.errors import InvalidId
# from django.utils.encoding import smart_text
# class ObjectIdField(serializers.Field):
#     """ Serializer field for Djongo ObjectID fields """
#     def to_internal_value(self, data):
#         # Serialized value -> Database value
#         try:
#             return ObjectId(str(data))  # Get the ID, then build an ObjectID instance using it
#         except InvalidId:
#             raise serializers.ValidationError('`{}` is not a valid ObjectID'.format(data))
#     def to_representation(self, value):
#         # Database value -> Serialized value
#         if not ObjectId.is_valid(value):  # User submitted ID's might not be properly structured
#             raise InvalidId
#         return smart_text(value)
from api.models import Problem
from api.serializers.UserSerializer import UserListContestSerializer


class ContestSerializer(DjongoModelSerializer):
    created_user = serializers.StringRelatedField()

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'description', 'created', 'created_user', 'time_start', 'time_end')
        # fields = '__all__'

    def create(self, validated_data):
        return Contest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
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


class ContestAttendedSerializer(DjongoModelSerializer):
    class Meta:
        model = Contest
        fields = ('_id', 'title')


class ContestListContestantsSerializer(DjongoModelSerializer):
    attended_contestants = UserIdSerializer(many=True)

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'attended_contestants')


class ContestListSerializer(DjongoModelSerializer):
    created_user = UserListContestSerializer()

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created', 'created_user', 'time_start', 'time_end')


class ProblemContestListSerializer(DjongoModelSerializer):
    languages = LanguageNameSerializer(many=True)

    class Meta:
        model = Problem
        fields = ('title', 'languages')


class ContestListWithProblemsSerializer(DjongoModelSerializer):
    problems = serializers.SerializerMethodField('get_problems')
    created_user = UserListContestSerializer()

    def get_problems(self, instance):
        query_id = instance._id
        data = Problem.objects.filter(contest_id=query_id)
        print(data.count())
        if data.count() != 0:
            problems = data.values('title')
            return problems
        problems = []
        return problems

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created', 'created_user', 'time_start', 'time_end', 'problems')
        extra_fields = ['problems']
# contest = Contest(title='bkdnContest 1')
# contest.save()
# serializer_class = ContestSerializer(contest)
# print(JSONRenderer().render(serializer_class.data))

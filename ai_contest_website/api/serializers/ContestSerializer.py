from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from djongo import models
from api.models import Contest
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from api.serializers.UserSerializer import UserIdSerializer
from api.serializers.UserSerializer import UserListContestSerializer
from api.serializers.LanguageSerializer import LanguageSerializer
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
class ContestSerializer(DjongoModelSerializer):
    created_user = ObjectIdField()
    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created' , 'created_user', 'time_start', 'time_end')
        # fields = '__all__'

    def create(self, validated_data):
        contest = Contest.objects.create(**validated_data)
        print('***************************')
        print(validated_data['created_user'])
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

class ContestAttendedSerializer(DjongoModelSerializer):
    class Meta:
        model = Contest
        fields = ('_id', 'title')

# contest = Contest(title='bkdnContest 1')
# contest.save()
# serializer_class = ContestSerializer(contest)
# print(JSONRenderer().render(serializer_class.data))
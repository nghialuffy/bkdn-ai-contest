from rest_meets_djongo.serializers import DjongoModelSerializer
from rest_meets_djongo import serializers as _serializers
from rest_framework import serializers
from api.models import Result, Problem, User, Language
from api.serializers.UserSerializer import UserSerializer, UserIdSerializer
from api.serializers.LanguageSerializer import LanguageSerializer, LanguageIdSerializer
from api.serializers.ProblemSerializer import ProblemSerializer, ProblemIdSerializer

from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

class ResultSerializer(DjongoModelSerializer):
    problem = _serializers.ObjectIdField()
    created_user = serializers.StringRelatedField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = ('_id', 'problem', 'created_user', 'model_file', 'code_test', 'code_train', 'accuracy', 'time_submit', 'language')

    def create(self, validated_data):
        return Result.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.problem = validated_data.get('problem', instance.problem)
        instance.created_user = validated_data.get('created_user', instance.created_user)
        instance.model_file = validated_data.get('model_file', instance.model_file)
        instance.code_test = validated_data.get('code_test', instance.code_test)
        instance.code_train = validated_data.get('code_train', instance.code_train)
        instance.accuracy = validated_data.get('accuracy', instance.accuracy)
        instance.time_submit = validated_data.get('time_submit', instance.time_submit)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return validated_data
class ResultSunmitSerializer(DjongoModelSerializer):
    problem = serializers.StringRelatedField()
    created_user = serializers.StringRelatedField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = ('_id', 'problem', 'created_user', 'model_file', 'code_test', 'code_train', 'language', 'time_submit')

    def create(self, validated_data):
        return Result.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.problem = validated_data.get('problem', instance.problem)
        instance.created_user = validated_data.get('created_user', instance.created_user)
        instance.model_file = validated_data.get('model_file', instance.model_file)
        instance.code_test = validated_data.get('code_test', instance.code_test)
        instance.code_train = validated_data.get('code_train', instance.code_train)
        instance.language = validated_data.get('language', instance.language)
        instance.time_submit = validated_data.get('time_submit', instance.time_submit)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return validated_data
# print("Create result")

# u = User.objects.get(username='nghialuffy')
# p = Problem.objects.get(title='problem 1')
# l1 = Language.objects.get(name='Python')
# r = Result()
# r.problem = p
# r.created_user = u
# r.language = l1
# r.save()
# r = Result.objects.get(_id= "6073b458dd246be6a5495169")
# serializers_r = ResultSerializer(r)
# print(JSONRenderer().render(serializers_r.data))
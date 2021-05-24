from rest_meets_djongo.fields import ObjectIdField, ArrayModelField
from rest_meets_djongo.serializers import DjongoModelSerializer
from api.models import Problem, Contest, Language
from django.http import JsonResponse
from rest_meets_djongo import serializers
from api.serializers.ContestSerializer import ContestSerializer, ContestIdSerializer
from api.serializers.LanguageSerializer import LanguageSerializer, LanguageIdSerializer
class ProblemSerializer(DjongoModelSerializer):
    contest = ContestSerializer()
    languages = LanguageSerializer(many=True)
    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'score', 
                'code_test', 'data_sample', 'train_data', 
                'test_data', 'time_executed_limit', 'contest', 'languages']

    def create(self, validated_data):
        return Problem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.contest = validated_data.get('contest', instance.contest)
        instance.languages = validated_data.get('languages', instance.languages)
        instance.description = validated_data.get('description', instance.description)
        instance.score = validated_data.get('score', instance.score)
        instance.code_test = validated_data.get('code_test', instance.code_test)
        instance.data_sample = validated_data.get('data_sample', instance.data_sample)
        instance.train_data = validated_data.get('train_data', instance.train_data)
        instance.test_data = validated_data.get('test_data', instance.test_data)
        instance.time_executed_limit = validated_data.get('time_executed_limit', instance.time_executed_limit)
        instance.save()
        return instance
        
    def validate(self, data):
        validated_data = data
        print('======= Valided ======')
        print(validated_data)
        return validated_data
class CreateProblemSerializer(DjongoModelSerializer):
    contest = serializers.drf_ser.StringRelatedField()
    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'score', 
                'code_test', 'data_sample', 'train_data', 
                'test_data', 'time_executed_limit', 'contest']

    def create(self, validated_data):
        return Problem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.contest = validated_data.get('contest', instance.contest)
        instance.description = validated_data.get('description', instance.description)
        instance.score = validated_data.get('score', instance.score)
        instance.code_test = validated_data.get('code_test', instance.code_test)
        instance.data_sample = validated_data.get('data_sample', instance.data_sample)
        instance.train_data = validated_data.get('train_data', instance.train_data)
        instance.test_data = validated_data.get('test_data', instance.test_data)
        instance.time_executed_limit = validated_data.get('time_executed_limit', instance.time_executed_limit)
        instance.save()
        return instance
        
    def validate(self, data):
        validated_data = data
        print('======= Valided ======')
        print(validated_data)
        return validated_data
class ProblemIdSerializer(DjongoModelSerializer):
    class Meta:
        model = Problem
        fields = ['_id']

    def create(self, validated_data):
        return Problem.objects.create(**validated_data)

# problem = Problem.objects.get(title="problem 1")
# contest = Contest.objects.get(title="bkdnContest 1")
# language = Language.objects.get(name='Python')
# problem.contest = contest
# problem.languages = [language]
# serializers_problem = ProblemSerializer(problem)
# print(JSONRenderer().render(serializers_problem.data))
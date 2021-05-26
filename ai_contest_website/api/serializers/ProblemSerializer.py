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


class CreateProblemSerializer(DjongoModelSerializer):
    contest = serializers.drf_ser.StringRelatedField()

    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'score', 
                'code_test', 'data_sample', 'train_data', 
                'test_data', 'time_executed_limit', 'contest']


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
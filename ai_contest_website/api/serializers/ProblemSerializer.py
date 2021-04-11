from rest_framework import serializers
from api.models import Problem
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('title', 'contest', 'languages', 'description', 'score', 'code_test', 'data_sample', 'train_data', 'test_data', 'time_executed_limit')

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

    def validate(self, data):
        validated_data = data
        return validated_data

# problem = Problem(title="Nghialuffy")
list_problem = Problem.objects.all()
serializer_class = ProblemSerializer(list_problem, many=True)
print(JSONRenderer().render(serializer_class.data))
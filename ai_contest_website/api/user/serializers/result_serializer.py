from rest_meets_djongo.serializers import DjongoModelSerializer
from rest_meets_djongo import serializers as _serializers
from rest_framework import serializers
from api.models import Result
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer


class UserResultWSSerializer(DjongoModelSerializer):
    problem = serializers.SlugRelatedField('title', read_only=True)
    created_user = serializers.StringRelatedField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = ('_id', 'created_user', 'problem', 'model_file', 'code_test', 'code_train', 'accuracy', 'time_submit',
                  'language', 'status', 'time_execute')

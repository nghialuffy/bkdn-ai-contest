from api.models import Result
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from rest_framework import serializers


class OrganizerResultProblemSerializer(DjongoModelSerializer):
    problem = serializers.SlugRelatedField('title', read_only=True)
    created_user = serializers.StringRelatedField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = ('_id', 'problem', 'created_user', 'model_file', 'code_test', 'code_train', 'accuracy', 'time_submit',
                  'language')

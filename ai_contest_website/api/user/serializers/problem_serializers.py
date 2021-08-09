from api.models import Problem
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from rest_framework.relations import StringRelatedField
from .language_serializers import UserLanguageSerializer


class UserProblemInfoSerializer(DjongoModelSerializer):
    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'time_executed_limit', 'contest', 'languages']

class UserProblemOnContestIdSerializer(DjongoModelSerializer):
    languages = UserLanguageSerializer(many=True)
    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'score','code_test',
            'data_sample', 'train_data', 'test_data','time_executed_limit', 'languages', ]
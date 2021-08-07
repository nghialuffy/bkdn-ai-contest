from api.models import Problem
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField


class UserProblemInfoSerializer(DjongoModelSerializer):
    class Meta:
        model = Problem
        fields = ['_id', 'title', 'description', 'time_executed_limit', 'contest', 'languages']

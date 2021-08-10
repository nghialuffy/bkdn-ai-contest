from api.models import Contest, Problem
from rest_framework import serializers
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from .problem_serializers import UserProblemInfoSerializer
from .user_serializers import UserInfoSerializer
class UserContestRegisterSerializer(DjongoModelSerializer):
    created_user = serializers.StringRelatedField()

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created_user', 'description', 'created', 'time_start', 'time_end')
        read_only_fields = ('created_user',)
        

class UserContestInfoSerializer(DjongoModelSerializer):
    created_user = serializers.StringRelatedField()

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created_user', 'description', 'created', 'time_start', 'time_end')
        read_only_fields = ('created_user',)

class UserContestWithProblemsSerializer(DjongoModelSerializer):
    problems = serializers.SerializerMethodField('get_problems')
    created_user = UserInfoSerializer()

    def get_problems(self, instance):
        query_id = instance._id
        data = Problem.objects.filter(contest_id=query_id)
        if data.count() != 0:
            problems = data.values('title')
            return problems
        problems = []
        return problems

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created', 'created_user', 'time_start', 'time_end', 'problems')
        extra_fields = ['problems']
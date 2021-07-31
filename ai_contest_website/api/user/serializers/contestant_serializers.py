from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from api.models.Contest import Contestant
from api.user.serializers.user_serializers import UserInfoSerializer
from api.user.serializers.contest_serializers import UserContestInfoSerializer
from api.models.User import User
from rest_meets_djongo import serializers

class UserContestRankSerializer(DjongoModelSerializer):
    user = UserInfoSerializer(read_only=True)
    class Meta:
        model = Contestant
        fields = ('_id', 'user', 'total_score')

    
class UserListAttendedContestsSerializer(DjongoModelSerializer):
    contest = UserContestInfoSerializer()
    class Meta:
        model = Contestant
        fields = ('_id', 'contest', 'total_score')

    def to_internal_value(self, data):
        return data
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from api.models.Contest import Contestant
from api.user.serializers.user_serializers import UserInfoSerializer


class UserContestRankSerializer(DjongoModelSerializer):
    user = UserInfoSerializer(read_only=True)
    class Meta:
        model = Contestant
        fields = ('_id', 'user', 'total_score')

    

    
    
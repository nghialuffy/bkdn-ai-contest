
from api.models.Contest import Contestant
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField
from api.organizer.serializers.user_serializers import OrganizerUserInfoSerializer

class OrganizerContestantsInContestSerializer(DjongoModelSerializer):
    user = OrganizerUserInfoSerializer()
    class Meta:
        model = Contestant
        fields = ('_id', 'user', 'total_score')
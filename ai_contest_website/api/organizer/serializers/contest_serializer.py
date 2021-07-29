from api.models import Contest
from rest_framework import serializers
from rest_meets_djongo.serializers import DjongoModelSerializer, ObjectIdField


class OrganizerContestSerializer(DjongoModelSerializer):
    created_user = serializers.StringRelatedField()

    class Meta:
        model = Contest
        fields = ('_id', 'title', 'created_user', 'description', 'created', 'time_start', 'time_end')
        read_only_fields = ('created_user',)
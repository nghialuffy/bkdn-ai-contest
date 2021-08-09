from api.models import Language
from rest_meets_djongo.serializers import DjongoModelSerializer


class OrganizerLanguageSerializer(DjongoModelSerializer):
    class Meta:
        model = Language
        fields = ['_id', 'name', 'file_extensions']


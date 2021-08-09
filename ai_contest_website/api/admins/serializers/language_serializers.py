from api.models import Language
from rest_meets_djongo.serializers import DjongoModelSerializer


class AdminLanguageSerializer(DjongoModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


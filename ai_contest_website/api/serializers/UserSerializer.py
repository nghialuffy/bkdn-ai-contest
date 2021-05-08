from rest_meets_djongo.serializers import DjongoModelSerializer
from rest_framework import serializers
from api.models import User
# from api.serializers import ContestAttendedSerializer


class UserSerializer(DjongoModelSerializer):
    # contest_attended_serializer = ContestAttendedSerializer(many=True)
    class Meta:
        model = User
        fields = ['_id', 'username', 'role', 'created', 'is_admin', 'is_organizer']
        extra_kwargs = {
            'url': {'view_name': 'user', 'lookup_field': 'username'},
            'users': {'lookup_field': 'username'}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.name)
        instance.role = validated_data.get('role', instance.role)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return validated_data


class UserLoginRespSerializer(DjongoModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'first_name', 'last_name', 'username']


class UserListContestSerializer(DjongoModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'first_name', 'last_name', 'username']


class UserIdSerializer(DjongoModelSerializer):
    class Meta:
        model = User
        fields = ['_id']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
    def get(self, validated_data):
        user = User.objects.get(**validated_data)


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'created']
        extra_kwargs = {
            'users': {'lookup_field': 'username'},
            'url': {'view_name': 'user', 'lookup_field': 'username'}
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        return validated_data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserContestAttendedSerializer(DjongoModelSerializer):
    # attended_contest = ContestAttendedSerializer()
    class Meta:
        model = User
        fields = ['username', 'attended_contest', 'first_name', 'last_name', 'created']

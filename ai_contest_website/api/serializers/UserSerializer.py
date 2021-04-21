from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'role', 'created']
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

class UserIdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['_id']
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

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
        # instance.role = 'user'
        instance.password = validated_data.get('password', instance.password)
        instance.first_name =validated_data.get('first_name', instance.first_name)
        instance.last_name =validated_data.get('last_name', instance.last_name)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    def validate(self, data):
        validated_data = data
        # validated_data['role'] = 'user'
        return validated_data
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'role', 'created')
    def __init__(self, meta):
        assert meta is not None, 'Meta cannot be None.'

        # assert hasattr(meta, 'start_index'), 'Meta.start_index is required.'
        # assert meta.start_index is not None, 'Must not be None.'
        # assert type(meta.start_index) is int, 'Must be int.'
        # self.start_index = meta.start_index

        # assert hasattr(meta, 'fields'), 'Meta.fields is required.'
        # assert meta.fields, 'Must not empty or None.'
        # assert type(meta.fields) in [list, tuple], 'Must be iteratable type list or tuple.'
        print(meta)
        self.fields = meta.fields

        # if hasattr(meta, 'enable_transaction'):
        #     assert type(meta.enable_transaction) in [None, bool], 'Type must be bool.'
        # self.enable_transaction = getattr(meta, 'enable_transaction', True)

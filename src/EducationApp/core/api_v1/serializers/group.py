from rest_framework import serializers
from .user import UserInfoSerializer


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    product = serializers.CharField()
    members = UserInfoSerializer(many=True)

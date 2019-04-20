from rest_framework import serializers
from .models import User


class CreateUser(serializers.Serializer):

    nick_name = serializers.CharField(required=True, allow_blank=False)
    avatar_url = serializers.CharField(required=True, allow_blank=False)
    # gender = serializers.IntegerField(required=False)
    open_id = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

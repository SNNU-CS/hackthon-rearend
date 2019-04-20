from .models import Activity, UserActivity
from rest_framework import serializers


class CreateActivitySerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    time = serializers.DateTimeField(required=True)
    location = serializers.CharField(required=True, allow_blank=True)
    activity_type = serializers.CharField(required=True, allow_blank=False)


class GetActivitySerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    time = serializers.DateTimeField(required=True)
    location = serializers.CharField(required=True, allow_blank=True)
    activity_type = serializers.CharField(required=True, allow_blank=False)
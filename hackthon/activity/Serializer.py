from .models import Activity, UserActivity
from rest_framework import serializers


class CreateActivitySerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    time = serializers.DateTimeField(required=True)
    location = serializers.CharField(required=True, allow_blank=True)
    activity_type = serializers.CharField(required=False, allow_blank=False)
    number = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Activity.objects.create(**validated_data)


class GetActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True, allow_blank=False)
    description = serializers.CharField(allow_blank=True)
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=True)
    location = serializers.CharField(required=True, allow_blank=True)
    activity_type = serializers.CharField(required=False, allow_blank=False)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            required=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            required=True)
    delete_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            required=True)
    number = serializers.IntegerField(required=True)
    number_now = serializers.IntegerField(required=True)


class GetUserActivitySerializer(serializers.Serializer):
    activity_id = serializers.IntegerField(required=True)
    user_class = serializers.CharField(required=True)

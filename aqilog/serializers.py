from rest_framework import serializers
from aqilog.models import Location, AQI


class AQISerializer(serializers.Serializer):
    created_at = serializers.DateTimeField()

    pm10 = serializers.IntegerField()
    pm25 = serializers.IntegerField()
    temperature = serializers.FloatField()
    no2 = serializers.IntegerField()
    aqi = serializers.IntegerField()
    so2 = serializers.IntegerField()
    w = serializers.IntegerField()
    co = serializers.IntegerField()
    p = serializers.IntegerField()
    h = serializers.IntegerField()
    o3 = serializers.IntegerField()


class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    country = serializers.CharField()
    url = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    current_condition = serializers.SerializerMethodField()

    def get_current_condition(self, obj):
        return AQISerializer(obj.aqi_set.last()).data


class LocationWithHistorySerializer(LocationSerializer):
    aqi_set = AQISerializer(many=True, read_only=True)


class AQIwithLocationSerializer(AQISerializer):
    location = LocationSerializer()

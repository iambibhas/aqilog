from aqilog.serializers import (
    LocationSerializer, LocationWithHistorySerializer,
    AQIwithLocationSerializer, AQISerializer
)
from aqilog.models import Location, AQI
from rest_framework import generics


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationInfo(generics.RetrieveAPIView):
    serializer_class = LocationWithHistorySerializer

    def get_object(self):
        return Location.objects.get(pk=self.kwargs.get('id'))

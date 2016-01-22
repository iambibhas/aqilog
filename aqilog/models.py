from django.db import models


class Location(models.Model):
    name = models.TextField()
    country = models.TextField()
    url = models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'location'


class AQI(models.Model):
    location = models.ForeignKey('Location')

    created_at = models.DateTimeField()

    pm10 = models.IntegerField(blank=True, null=True)
    pm25 = models.IntegerField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    no2 = models.IntegerField(blank=True, null=True)
    aqi = models.IntegerField(blank=True, null=True)
    so2 = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    co = models.IntegerField(blank=True, null=True)
    p = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    o3 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s at %s" % (self.location, self.created_at)

    class Meta:
        db_table = 'aqi'

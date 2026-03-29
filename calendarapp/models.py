from django.db import models

# Create your models here.

class Weather(models.Model):
    pass

class Event(models.Model):
    WEATHER_CHOICES = (
        ('SUNNY', 'Sunny'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    weather_required = models.CharField(max_length=40, choices=WEATHER_CHOICES, blank=True)

    def __str__(self):
        return self.title

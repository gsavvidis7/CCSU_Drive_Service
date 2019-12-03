from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Driver(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()

    def __int__(self):
        return self.id


class Rider(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    rider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __int__(self):
        return self.id

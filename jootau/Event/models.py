from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Location(models.Model):
    '''Defines location of the events'''
    name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class EventType(models.Model):
    '''stores category of the event'''
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    '''stores subscription type and category'''
    location = models.ForeignKey(Location, blank=True, null=True)
    event_type = models.ForeignKey(EventType, blank=True, null=True)

    def __unicode__(self):
        return self.location.name + " " + self.event_type.name


class GeneralUser(models.Model):
    '''stores information of the subscriber and general users'''
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=30, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    subscription = models.ManyToManyField(Subscription, blank=True, null=True)

    def __unicode__(self):
        return self.user.username


class Event(models.Model):
    '''stores description of the event'''
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location_name = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    event_type = models.ForeignKey(EventType, blank=True, null=True)
    host = models.ForeignKey(GeneralUser, blank=True, null=True,
                             related_name="host")
    participant = models.ManyToManyField(GeneralUser, blank=True, null=True,
                                         related_name="participant")

    def __unicode__(self):
        return self.title
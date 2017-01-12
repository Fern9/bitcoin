from __future__ import unicode_literals

from django.db import models


# Create your models here.


class OKCoinSpot(models.Model):
    date_stamp = models.FloatField()
    date_local = models.DateTimeField(auto_now=True, null=True)
    date_time = models.DateTimeField()
    buy = models.FloatField()
    high = models.FloatField()
    last = models.FloatField()
    low = models.FloatField()
    sell = models.FloatField()
    vol = models.FloatField()
    symbol = models.CharField(max_length=20, null=True)


class HuobiSpot(models.Model):
    date_stamp = models.FloatField()
    date_local = models.DateTimeField(auto_now=True, null=True)
    date_time = models.DateTimeField()
    buy = models.FloatField()
    high = models.FloatField()
    last = models.FloatField()
    low = models.FloatField()
    sell = models.FloatField()
    vol = models.FloatField()
    open = models.FloatField()
    symbol = models.CharField(max_length=20, null=True)


class Config(models.Model):
    key = models.CharField(max_length=50)
    value = models.TextField(default='')

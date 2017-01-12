from __future__ import unicode_literals

from django.db import models

# Create your models here.


class OKCoinSpot(models.Model):
    date_stamp = models.FloatField()
    date_local = models.DateTimeField(null=True)
    buy = models.FloatField()
    high = models.FloatField()
    last = models.FloatField()
    low = models.FloatField()
    sell = models.FloatField()
    vol = models.FloatField()
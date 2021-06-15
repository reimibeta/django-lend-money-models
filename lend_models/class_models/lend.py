from decimal import Decimal

from datetime_utils.date_time import DateTime
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from lends.class_models.lend_client import LendClient


class Lend(models.Model):
    client = models.ForeignKey(LendClient, on_delete=models.CASCADE)
    lend_date = models.DateField(default=DateTime.datenow)

    def __str__(self):
        return "{}({})".format(self.client, self.lend_date)

from django.db import models
from django.db.models.signals import post_save

from .contact import Contact

class Subscription(models.Model):
    subscription = models.CharField(max_length=100)
    members = models.ManyToManyField(Contact)

    def __str__(self):
        return '{}'.format(self.subscription)

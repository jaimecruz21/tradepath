from django.db import models
from django.db.models.signals import post_save

from .contact import Contact

class Membership(models.Model):
    contact = models.ForeignKey(Contact)
    subscription = models.ForeignKey(Subscription)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.subscription, self.contact)

from django.db import models
from django.db.models.signals import post_save

from .path import Path
from .condition import Condition
from .contact import Contact
from .subscription import Subscription

class Request(models.Model):
    condition = models.ForeignKey(Condition, null=True, blank=True)
    path = models.ManyToManyField(Path)
    approval_subscription = models.ForeignKey(Subscription, null=True, blank=True)
    approved_on = models.DateField(null=True, blank=True)
    approved_by = models.ForeignKey(Contact, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.condition, self.approval_subscription)

# post_save.connect(create_requirements, sender=Portfolio)

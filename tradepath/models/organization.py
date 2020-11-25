from django.db import models
from django.db.models.signals import post_save

class Organization(models.Model):
    name = models.CharField(max_length=100)
    is_counterparty = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return '{}'.format(self.name)

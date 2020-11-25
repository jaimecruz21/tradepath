from django.db import models
from django.db.models.signals import post_save

from .organization import Organization

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.CASCADE
                                     )

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email_address)

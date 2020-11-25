from django.db import models
from django.contrib.postgres.fields import ArrayField

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    parent_portfolio = models.CharField(max_length=50, null=True, blank=True)
    portfolio_type = models.CharField(max_length=50, null=True, blank=True)
    rules = ArrayField(ArrayField(
            models.CharField(max_length=50, null=True, blank=True),
        ), size=8, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

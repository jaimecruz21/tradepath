from django.db import models

from .issuer import Issuer

class Investment(models.Model):
    INVESTMENT_TYPES = (
        ('BANK_LOAN', 'Bank Loan'),
        ('BOND', 'Bond'),
        ('EQUITY', 'Equity'),
        ('OTHER', 'Other'),
    )

    issuer = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    investment_type = models.CharField(
        max_length=15,
        choices=INVESTMENT_TYPES,
        default='OTHER',
        null=True
    )
    base = models.FloatField(null=True, blank=True)
    spread = models.FloatField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateField(auto_now=True, null=True, blank=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

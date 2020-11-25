from django.db import models

from .trade import Trade
from .portfolio import Portfolio

class Allocation(models.Model):
    STATUSES = (
        ('PENDING', 'Pending'),
        ('READY', 'Ready'),
        ('SETTLED', 'Settled'),
        ('HOLD', 'On Hold'),
        ('UPSTREAM', 'Upstream'),
    )

    trade = models.ForeignKey(Trade, related_name='allocations', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    quantity = models.FloatField()
    coinvest = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=STATUSES,
        default='PENDING',
    )
    settle_date = models.DateField(null=True)
    venue_allocation_id = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} | [{}] {}  on {}'.format(self.portfolio, self.trade.action,
                                                self.trade.investment.name, self.trade.trade_date)

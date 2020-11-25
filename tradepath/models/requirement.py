from django.db import models
from django.db.models.signals import post_save

from .portfolio import Portfolio
from .condition import Condition
from .subscription import Subscription

class Requirement(models.Model):
    portfolio =  models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    approval_subscription = models.ForeignKey(Subscription, null=True, blank=True, related_name='approval_subscription')
    notification_subscription = models.ForeignKey(Subscription, null=True, blank=True, related_name='notification_subscription')
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.portfolio.name, self.condition.name)

def create_requirements(sender, **kwargs):
    instance = kwargs['instance']
    print('\n> Adding Portfolio Requirements', instance, '\n')
    conditions = Condition.objects.all()

    for condition in conditions:
        print('\t', condition)
        Requirement.objects.create(portfolio=instance, condition=condition)


post_save.connect(create_requirements, sender=Portfolio)

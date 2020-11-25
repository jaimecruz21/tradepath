from django.db import models
from django.db.models.signals import post_save

from .allocation import Allocation
from .requirement import Requirement

class Path(models.Model):

    STATUSES = (
        ('PENDING', 'Pending'),
        ('IN PROGRESS', 'In Progress'),
        ('NOT CIRCULATED', 'Not Circulated'),
        ('N/A', 'N/A'),
        ('COMPLETED', 'Completed'),
    )

    allocation = models.ForeignKey(Allocation, on_delete=models.CASCADE)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=STATUSES,
        default='PENDING',
    )
    completed_on = models.DateField(null=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{} > {}'.format(self.requirement, self.allocation.trade.investment.name)

def create_actions(sender, **kwargs):
    instance = kwargs['instance']
    print('\n>', instance, '\n')
    q = Requirement.objects.all().filter(portfolio=instance.portfolio)

    Path.objects.filter(allocation=instance).delete()

    for r in q:
        print('\t', r.condition)

        entity = r.condition.entity
        entity_field = r.condition.entity_field
        entity_field_value = r.condition.entity_field_value

        if (entity != None):
            print('\t\t> Entity Condition:', '{}[{}] == {}'.format(entity, entity_field, entity_field_value))

            if (entity == 'portfolio'):
                instance_entity = getattr(instance, entity)
                instance_entity_field_value = getattr(instance_entity, entity_field)

            if (entity == 'investment'):
                instance_entity = getattr(getattr(instance, 'trade'), entity)
                instance_entity_field_value = getattr(instance_entity, entity_field)

            if (entity == 'trade'):
                instance_entity = getattr(instance, entity)
                instance_entity_field_value = getattr(instance_entity, entity_field)

            if (instance_entity_field_value == entity_field_value):
                Path.objects.create(allocation=instance, requirement=r)

        else:
            print('\t\t> Default')
            Path.objects.create(allocation=instance, requirement=r)

post_save.connect(create_actions, sender=Allocation)

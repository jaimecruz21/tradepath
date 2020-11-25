from django.db import models

class Condition(models.Model):

    CONDITION_TYPES = (
        ('TASK', 'Task'),
        ('ACTIVITY', 'Activity'),
        ('APPROVAL', 'Approval'),
        ('CONFIRMATION', 'Confirmation'),
    )

    ENTITIES = (
        (None, 'None'),
        ('portfolio', 'Portfolio'),
        ('allocation', 'Allocation'),
        ('trade', 'Trade'),
        ('investment', 'Investment'),
        ('counterparty', 'Counterparty'),
    )

    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    entity = models.CharField(
            max_length=50,
            choices=ENTITIES,
            default=None,
            null=True,
            blank=True
        )
    entity_field = models.CharField(max_length=100, null=True, blank=True)
    entity_field_value = models.CharField(max_length=100, null=True, blank=True)
    condition_group = models.CharField(max_length=100, null=True, blank=True)
    condition_type = models.CharField(
            max_length=50,
            choices=CONDITION_TYPES,
            default='Task'
        )

    sort_order = models.IntegerField()
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{} | {}'.format(self.name, self.sort_order)

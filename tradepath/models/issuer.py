from django.db import models

class Issuer(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True, null=True)
    updated_on = models.DateField(auto_now=True, null=True)
    external_id = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

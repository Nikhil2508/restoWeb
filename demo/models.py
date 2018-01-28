from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Demo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

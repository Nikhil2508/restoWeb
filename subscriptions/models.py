from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SubscriptionType(models.Model):
    # name
    # user
    # allowedProducts

class SubscriptionItems(models.Model):
    # subscriptionType
    # items--->foriegnKey of variation
    

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=8)
    last_name = models.CharField(max_length=8)
    contact_number = models.IntegerField(default=0)
    is_active = models.BooleanField
    dob = models.DateField


    def __str__ (self):
        return self.first_name
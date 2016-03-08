from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True)

    first_name = models.CharField(
        max_length=8,
        blank=False,
        null=False)

    last_name = models.CharField(
        max_length=8,
        null=False,
        blank=False)

    contact_number = models.IntegerField(default=0)
    is_active = models.BooleanField
    dob = models.DateField

    def __str__(self):
        return self.first_name


class Address(models.Model):

    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='addresses')

    address_line_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    address_line_1 = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )

    building_no = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    floor_no = models.IntegerField(
        blank=True,
        null=True
    )

    house_no = models.CharField(
        max_length=25,
        blank=False,
        null=False
    )

    city = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    state = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    pin_code = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )






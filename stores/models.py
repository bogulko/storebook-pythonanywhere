from __future__ import unicode_literals

from django.db import models

class municipality(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=100,null=True)
    muniID = models.IntegerField()
    population = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand = models.CharField(max_length=50, unique = True)
    operator = models.CharField(max_length=50)

    def __str__(self):
        return self.brand

class Stores(models.Model):
    fascia = models.ForeignKey(Brand, on_delete = models.CASCADE)
    store_format = models.CharField(max_length=30, blank=True, null=True)  # Field name made lowercase.
    town = models.ForeignKey(municipality, on_delete = models.CASCADE)
    street_adr = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fascia.brand + ' - ' + str(self.town.name) + ', ' + self.street_adr

# Create your models here.

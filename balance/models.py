from __future__ import unicode_literals
from django.db import models
# import time

# Create your models here.


class User(models.Model):
    joiningDate = models.DateTimeField()
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return str(self.joiningDate) + " " + self.name + " " + self.gender + " " + self.email + " " + str(self.balance)
        # return ' '.joinn([str(self.joiningDate), self.name, self.gender, self.email, str(self.balance)])


class Activity(models.Model):
    date = models.DateTimeField()
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    individuelCost = models.DecimalField(max_digits=10, decimal_places=2)
    people = models.TextField(max_length=2000)
    note = models.TextField(max_length=2000, blank=True)

    def __unicode__(self):
        return str(self.date) + " cost " + str(self.totalCost) + " by " + self.people + "(" + str(self.individuelCost) + " per person) " + " Note: " + self.note
        # return ' '.join([str(self.date), 'cost', str(self.totalCost), 'by', self.people, "(" + str(self.individuelCost), 'per person)', 'Note:', self.note])

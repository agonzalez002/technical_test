from django.db import models


class Person(models.Model):
    """Model class for person"""
    lastname = models.CharField(max_length=250)
    firstname = models.CharField(max_length=250)
    birthday = models.DateField()

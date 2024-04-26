from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(max_length=200)
    experience = models.IntegerField()


class Executor(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(max_length=200)
    experience = models.IntegerField()


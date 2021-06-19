from django.db import models

class Students(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(max_length=200)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=200)


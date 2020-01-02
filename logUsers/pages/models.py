from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Person(models.Model):
#     #personId    = models.AutoField(primary_key=True, default=0)
#     first_name  = models.CharField(max_length=30, null=True)
#     last_name   = models.CharField(max_length=150, null=True)
#     username    = models.CharField(max_length=100, null=True)
#     password    = models.CharField(max_length=100, null=True)

class PersonLog(models.Model):
    #logId       = models.AutoField(primary_key=True, default=0)
    #personId    = models.ForeignKey(Person, on_delete=models.CASCADE, default=0)
    personId    = models.IntegerField() #migrate
    timeIn      = models.DateTimeField(null=True, auto_now=True)
    timeOut     = models.DateTimeField(null=True)


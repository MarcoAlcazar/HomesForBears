from django.db import models
from django import forms

# Create your models here.
class Housing(models.Model):
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length = 250)
    Rating = models.IntegerField(0-10)
    Price = models.IntegerField()
    LandLord = models.CharField(max_length = 200, default = "none")


class Landlord(models.Model):
    FullName= models.CharField(max_length = 60, default = "none")
    Rating = models.IntegerField()
    Description = models.CharField(max_length = 250)



     
    


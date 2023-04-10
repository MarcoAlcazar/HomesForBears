from django.db import models
from django import forms

# Create your models here.
class Housing(models.Model):
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length = 250, default="none")
    Rating = models.IntegerField(default = "none")
    Price = models.IntegerField(default="0")
    LandLord = models.CharField(max_length = 200, default = "none")


class Landlord(models.Model):
    FullName= models.CharField(max_length = 60, default = "none")
    Rating = models.IntegerField(default = 0)
    Description = models.CharField(max_length = 250, default = "none")



     
    


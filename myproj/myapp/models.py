from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Housing(models.Model):
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length = 250, default="")
    Rating = models.IntegerField(default = "", validators=[MinValueValidator(1), MaxValueValidator(5)])
    Price = models.IntegerField(default="")
    LandLord = models.CharField(max_length = 200, default = "")


class Landlord(models.Model):
    FullName= models.CharField(max_length = 60, default = "")
    Rating = models.IntegerField(default = "", validators=[MinValueValidator(1), MaxValueValidator(5)])
    Description = models.CharField(max_length = 250, default = "")



     
    


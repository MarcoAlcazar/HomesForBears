from django.db import models

# Create your models here.
class Landlord(models.Model):
    First_Name= models.CharField(max_length = 25)
    Last_Name = models.CharField(max_length = 25)
    Rating = models.IntegerField()
    Description = models.CharField(max_length = 250)
    

class Housing(models.Model):
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length = 250)
    Rating = models.IntegerField()
    price = models.IntegerField()
    LandLord = models.CharField(max_length = 200)



from django.db import models

# Create your models here.
class Housing(models.Model):
    Address = models.CharField(max_length=50)

class HousingReview(models.Model):
    Address = models.ForeignKey(Housing, on_delete= models.CASCADE)
    Description = models.CharField(max_length = 250)
    Rating = models.IntegerField()
    price = models.IntegerField()
    LandLord = models.CharField(max_length = 200, default = "none")


class Landlord(models.Model):
    FullName= models.CharField(max_length = 60, default = "none")
    
class LandlordReview(models.Model):
    Landlord = models.ForeignKey(Landlord, on_delete= models.CASCADE)
    Rating = models.IntegerField()
    Description = models.CharField(max_length = 250)
    


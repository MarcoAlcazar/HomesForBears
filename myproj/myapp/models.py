from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image 
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


# Create your models here.
def resize_image(image, max_width=500, max_height=500):
    img = Image.open(image)
    
    # Check if the 'ANTIALIAS' attribute exists
    try:
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)
    except AttributeError:
        # For newer Pillow versions, use 'thumbnail()' directly
        img.thumbnail((max_width, max_height))
    
    img.save(image.path)

class Housing(models.Model):
    # ... Your other model fields ...
    Address = models.CharField(max_length=50)
    Bedrooms = models.IntegerField(default="", validators=[MinValueValidator(1), MaxValueValidator(25)])
    Bathrooms = models.IntegerField(default="", validators=[MinValueValidator(1), MaxValueValidator(25)])
    Description = models.CharField(max_length=250, default="")
    Rating = models.IntegerField(default="", validators=[MinValueValidator(1), MaxValueValidator(5)])
    Price = models.IntegerField(default="", validators=[MinValueValidator(500), MaxValueValidator(50000)])
    LandLord = models.CharField(max_length=200, default="")
    housing_image = models.ImageField(null=True, blank=True, upload_to="images/")
    housing_image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    housing_image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    housing_image4 = models.ImageField(null=True, blank=True, upload_to="images/")
    housing_image5 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        # Define how you want the object to be displayed
        return self.Address

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.housing_image:
            resize_image(self.housing_image)
        if self.housing_image2:
            resize_image(self.housing_image2)
        if self.housing_image3:
            resize_image(self.housing_image3)
        if self.housing_image4:
            resize_image(self.housing_image4)
        if self.housing_image5:
            resize_image(self.housing_image5)

class Landlord(models.Model):
    FullName= models.CharField(max_length = 60, default = "")
    Rating = models.IntegerField(default = "", validators=[MinValueValidator(1), MaxValueValidator(5)])
    Description = models.CharField(max_length = 250, default = "")

    def __str__(self):
        # Define how you want the object to be displayed
        return self.FullName




     
    


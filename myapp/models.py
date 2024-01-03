from django.db import models
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image 
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        self.resize_images()

    def resize_images(self):
        # Sample implementation using PIL to resize images
        if self.housing_image:
            self.resize_image(self.housing_image)
        if self.housing_image2:
            self.resize_image(self.housing_image2)
        if self.housing_image3:
            self.resize_image(self.housing_image3)
        if self.housing_image4:
            self.resize_image(self.housing_image4)
        if self.housing_image5:
            self.resize_image(self.housing_image5)

    def resize_image(self, image_field):
        # Sample implementation using PIL to resize an image
        image = Image.open(image_field)
        output = io.BytesIO()
        image = image.resize((300, 300))  # Adjust the size as needed
        image.save(output, format='JPEG', quality=90)
        output.seek(0)
        image_field.file = InMemoryUploadedFile(output, 'ImageField', f"{image_field.name.split('.')[0]}_resized.jpg",
                                        'image/jpeg', output.tell(), None)



     
    


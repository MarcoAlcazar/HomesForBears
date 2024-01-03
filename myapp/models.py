from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import json
import boto3
from django.core.files.uploadedfile import InMemoryUploadedFile
from botocore.exceptions import NoCredentialsError
import io


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

def upload_to_s3(data, filename, folder):
    """
    Upload data to an S3 bucket.
    """
    S3_BUCKET = 'homesforbears'

    # Initialize the S3 client
    s3 = boto3.client('s3', aws_access_key_id='AKIAW3TQQ24DWM5MXPNB', aws_secret_access_key='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')

    try:
        # Upload data to S3
        s3.put_object(Body=data, Bucket=S3_BUCKET, Key=f'{folder}/{filename}')
    except NoCredentialsError:
        print("Credentials not available")

class Housing(models.Model):
    # ... Your other model fields ...

    def __str__(self):
        # Define how you want the object to be displayed
        return self.Address

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_images()

        # Convert housing data to JSON format
        housing_data = {
            'address': self.Address,
            'bedrooms': self.Bedrooms,
            'bathrooms': self.Bathrooms,
            'description': self.Description,
            'rating': self.Rating,
            'price': self.Price,
            'landlord': self.LandLord,
        }
        housing_data_json = json.dumps(housing_data)

        # Upload housing data to S3
        upload_to_s3(housing_data_json, f'{self.id}_housing.json', 'housing')

        # Upload landlord data to S3
        landlord_data = {
            'full_name': self.LandLord.FullName,
            'rating': self.LandLord.Rating,
            'description': self.LandLord.Description,
        }
        landlord_data_json = json.dumps(landlord_data)

        # Upload landlord data to S3
        upload_to_s3(landlord_data_json, f'{self.id}_landlord.json', 'landlord')

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

class Landlord(models.Model):
    FullName = models.CharField(max_length=60, default="")
    Rating = models.IntegerField(default="", validators=[MinValueValidator(1), MaxValueValidator(5)])
    Description = models.CharField(max_length=250, default="")

    def __str__(self):
        # Define how you want the object to be displayed
        return self.FullName





     
    


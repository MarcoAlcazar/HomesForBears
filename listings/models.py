from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import json
import boto3
from django.core.files.uploadedfile import InMemoryUploadedFile
from botocore.exceptions import NoCredentialsError
import io


def upload_to_s3(data, filename, folder):
    S3_BUCKET = 'homesforbears'
    s3 = boto3.client('s3', aws_access_key_id='AKIAW3TQQ24DWM5MXPNB', aws_secret_access_key='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')
    try:
        s3.put_object(Body=data, Bucket=S3_BUCKET, Key=f'{folder}/{filename}')
    except NoCredentialsError:
        print("Credentials not available")


class Housing(models.Model):
    Address = models.CharField(max_length=50)
    Description = models.CharField(max_length=250, default='')
    Rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    Price = models.IntegerField(default=0)
    LandLord = models.CharField(max_length=200, default='')
    Bedrooms = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(25)])
    Bathrooms = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(25)])
    housing_image = models.ImageField(upload_to='images/', null=True, blank=True)
    housing_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    housing_image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    housing_image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    housing_image5 = models.ImageField(upload_to='images/', null=True, blank=True)
    submitted_by = models.CharField(max_length=150, blank=True, default='')

    def __str__(self):
        return self.Address

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_images()
        housing_data = {
            'address': self.Address,
            'bedrooms': self.Bedrooms,
            'bathrooms': self.Bathrooms,
            'description': self.Description,
            'rating': self.Rating,
            'price': self.Price,
            'landlord': self.LandLord,
        }
        upload_to_s3(json.dumps(housing_data), f'{self.id}_housing.json', 'housing')

    def resize_images(self):
        for field in [self.housing_image, self.housing_image2, self.housing_image3,
                      self.housing_image4, self.housing_image5]:
            if field:
                self.resize_image(field)

    def resize_image(self, image_field):
        image = Image.open(image_field)
        output = io.BytesIO()
        image = image.resize((300, 300))
        image.save(output, format='JPEG', quality=90)
        output.seek(0)
        size = len(output.getvalue())
        image_field.file = InMemoryUploadedFile(
            output, 'ImageField',
            f"{image_field.name.split('.')[0]}_resized.jpg",
            'image/jpeg', size, None,
        )


class Landlord(models.Model):
    FullName = models.CharField(max_length=60, default='')
    Rating = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    Description = models.CharField(max_length=250, default='')
    submitted_by = models.CharField(max_length=150, blank=True, default='')

    def __str__(self):
        return self.FullName

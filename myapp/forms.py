from django import forms

from myapp.models import Landlord
from myapp.models import Housing



class LandlordForm(forms.ModelForm):
   class Meta:
     model = Landlord
     fields = ('FullName', 'Description', 'Rating')
     labels = {
      'FullName' :'', 
      'Description' :'',
      'Rating' :'',
     }
     widgets = {
      'FullName' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter LandLords Full Name, Example: Hugh Manatee', 'style': 'color: #555; height: 50px; width: 300px; resize: none;'}),
      'Description' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'style': 'height: 200px; width: 400px; resize: none;'}),
      'Rating' :forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter Rating (Number From 1-5)', 'style': 'height: 50px; width: 300px; resize: none;'}),
     }

class HousingForm(forms.ModelForm):
    class Meta:
        model = Housing
        fields = ('address', 'bedrooms', 'bathrooms', 'description', 'rating', 'price', 'landLord', 'housing_image', 'housing_image2', 'housing_image3', 'housing_image4', 'housing_image5')
        labels = {
            'address': '',
            'bedrooms': '',  
            'bathrooms': '',
            'description': '',
            'rating': '',
            'price': '',
            'landLord': '',
            'housing_image': 'Please insert your main image',
            'housing_image2': 'Please insert an image',
            'housing_image3': 'Please insert an image',
            'housing_image4': 'Please insert an image',
            'housing_image5': 'Please insert an image',
        }
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'style': 'color: #555; height: 50px; width: 300px; resize: none;'}),
            'bedrooms': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Bedrooms', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'bathrooms': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Bathrooms', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'style': 'height: 200px; width: 400px; resize: none;'}),
            'rating': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Rating (Number From 1-5)', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'price': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter how much you pay per month', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'landLord': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter LandLords Full Name, Example: Hugh Manatee', 'style': 'height: 50px; width: 300px; resize: none;'}),
        }

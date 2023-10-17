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
        fields = ('Address', 'Description', 'Rating', 'Price', 'LandLord', 'housing_image')
        labels = {
            'Address': '',
            'Description': '',
            'Rating': '',
            'Price': '',
            'LandLord': '',
            'housing_image': 'Upload an Image',
        }
        widgets = {
            'Address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'style': 'color: #555; height: 50px; width: 300px; resize: none;'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'style': 'height: 200px; width: 400px; resize: none;'}),
            'Rating': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Rating (Number From 1-5)', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'Price': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Price Per Month', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'LandLord': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter LandLords Full Name, Example: Hugh Manatee', 'style': 'height: 50px; width: 300px; resize: none;'}),
            'housing_image': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*','style': 'height: 50px; width: 300px; resize: none;' })  # Use the FileInput widget
        }
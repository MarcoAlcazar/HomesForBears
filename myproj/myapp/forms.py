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
      'FullName' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter LandLords Full Name', 'style': 'color: #555; height: 50px; width: 300px; resize: none;'}),
      'Description' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'style': 'height: 200px; width: 400px; resize: none;'}),
      'Rating' :forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter Rating', 'style': 'height: 50px; width: 300px; resize: none;'}),
     }

class HousingForm(forms.ModelForm):
   class Meta:
      model = Housing
      fields = ('Address', 'Description', 'Rating', 'Price', 'LandLord')
      labels = {
        'Address' :'', 
        'Description' :'',
        'Rating' :'',
        'Price' :'',
        'LandLord' :'',
      }
      widgets = {
        'Address' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'style': 'color: #555; height: 50px; width: 300px; resize: none;'}),
        'Description' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'style': 'height: 200px; width: 400px; resize: none;'}),
        'Rating' :forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter Rating', 'style': 'height: 50px; width: 300px; resize: none;'}),
        'Price' :forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Price Per Month', 'style': 'height: 50px; width: 300px; resize: none;'}),
        'LandLord' :forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter LandLords Full Name', 'style': 'height: 50px; width: 300px; resize: none;'}),
      }
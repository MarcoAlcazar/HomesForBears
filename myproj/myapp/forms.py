from django import forms

from myapp.models import Landlord
from myapp.models import Housing

class LandlordForm(forms.ModelForm):
   class Meta:
     model = Landlord
     fields = '__all__' 

class HousingForm(forms.ModelForm):
   class Meta:
     model = Housing
     fields = '__all__' 
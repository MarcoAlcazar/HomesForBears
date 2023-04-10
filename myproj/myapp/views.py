from django.shortcuts import render
from django.http import HttpResponse
from .models import Landlord
from .models import Housing
from django.template import loader
from myapp.forms import LandlordForm
from myapp.forms import HousingForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def create_review(request): 
    return render(request, 'myapp/create_review.html')

def apartments(request):
   return render(request, 'myapp/apartments.html')

def about_us(request):
   return render(request, 'myapp/about_us.html')

def review(request):
   return render(request, 'myapp/Review_create.html')

def Landlord_create(request):
   form = LandlordForm()
   return render(request,
            'myapp/Landlord_create.html',
            {'form': form})

def Housing_create(request):
    if request.method == "POST":
        form  = HousingForm(request.POST)
        if form.is_valid():
            housing = form.save()
            return redirect('housing-detail', housing.id)
    else:
        form = HousingForm()
    return render(request,
                'myapp/Housing_create.html',
                {'form': form})



from django.shortcuts import render
from django.http import HttpResponse
from .models import Landlord
from .models import LandlordReview
from .models import Housing
from .models import HousingReview
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def create_review(request): 
    return render(request, 'myapp/create_review.html')



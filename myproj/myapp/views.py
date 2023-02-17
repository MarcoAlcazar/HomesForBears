from django.shortcuts import render
from django.http import HttpResponse
from .models import Landlord
from .models import LandlordReview
from .models import Housing
from .models import HousingReview
from django.template import loader

# Create your views here.
def index(request):
    latest_names_list = Landlord.objects.all()
    context = {'latest_names_list': latest_names_list}
    return render(request, 'myapp/index.html', context)


def NameofLandlord(request, LandlordName):
    return HttpResponse("Youre looking at %s." % LandlordName)

def LandlordReviewList(request, LandlordName):
    response = "Youre looking at the reviews of %s."
    return HttpResponse(response % LandlordName)

def ApartmentAddress(request, Address):
    return HttpResponse("Youre looking at the place located in %s." % Address)

def ApartmentReviewList(request, Address):
    response = "Youre looking at the reviews of %s."
    return HttpResponse(response % Address)


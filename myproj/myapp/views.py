from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

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


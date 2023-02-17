from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def detail(request, landlords):
    return HttpResponse("Youre looking at %s." % landlords)

def detail(request, apartment):
    return HttpResponse("Youre looking at %s." % apartment)


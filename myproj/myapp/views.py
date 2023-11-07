from django.shortcuts import render
from django.http import HttpResponse
from .models import Landlord
from .models import Housing
from django.template import loader
from myapp.forms import LandlordForm
from myapp.forms import HousingForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def search_apartments(request):
    if request.method == "POST": 
        searched = request.POST.get('searched')
        apartments = Housing.objects.filter(Address__contains= searched)
        return render(request, 'myapp/search_apartment.html', {'searched' : searched, 'apartments': apartments })
    else:
        return render(request, 'myapp/search_apartment.html')

    
def search_landlords(request):
    if request.method == "POST": 
        searched = request.POST.get('searched')
        landlords = Landlord.objects.filter(FullName__contains= searched)
        return render(request, 'myapp/search_landlords.html', {'searched' : searched, 'landlords': landlords })
    else:
        return render(request, 'myapp/search_landlords.html')

def show_landlord(request, landlord_id):
    user_username = request.session.get('user_username', None)
    landlord = Landlord.objects.get(pk = landlord_id)
    return render(request, 'myapp/show_landlord.html',{'landlord': landlord,  'user_username': user_username} )

def show_house(request, house_id):
    user_username = request.session.get('user_username', None)
    house = Housing.objects.get(pk = house_id)
    return render(request, 'myapp/show_house.html',{'house': house, 'user_username': user_username} )

def index(request):
    return render(request, 'myapp/index.html')

def create_review(request): 
    return render(request, 'myapp/create_review.html')

class apartmentss(ListView):
   template_name = 'myapp/apartmentss.html'
   context_object_name = 'apartmentss'
   model = Housing
   paginate_by = 6


   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)


       # Get all apartments
       apartment_queryset = Housing.objects.all()


       # Paginate the apartment queryset
       apartment_paginator = Paginator(apartment_queryset, self.paginate_by)


       # Get the current page number for apartments
       apartment_page = self.request.GET.get('apartment_page')


       try:
           apartments = apartment_paginator.get_page(apartment_page)
       except PageNotAnInteger:
           apartments = apartment_paginator.get_page(1)
       except EmptyPage:
           apartments = apartment_paginator.get_page(apartment_paginator.num_pages)


       context['apartments'] = apartments


       # Get all landlords
       landlord_queryset = Landlord.objects.all()


       # Paginate the landlord queryset
       landlord_paginator = Paginator(landlord_queryset, self.paginate_by)


       # Get the current page number for landlords
       landlord_page = self.request.GET.get('landlord_page')


       try:
           landlords = landlord_paginator.get_page(landlord_page)
       except PageNotAnInteger:
           landlords = landlord_paginator.get_page(1)
       except EmptyPage:
           landlords = landlord_paginator.get_page(landlord_paginator.num_pages)


       context['landlords'] = landlords


       return context

def about_us(request):
   return render(request, 'myapp/about_us.html')

def review(request):
   return render(request, 'myapp/Review_create.html')

def thankyou(request):
   return render(request, 'myapp/thankyou.html')

def Housing_create(request):
    if request.method == "POST":
        request.session['user_username'] = request.user.username
        form  = HousingForm(request.POST, request.FILES)
        if form.is_valid():
            housing = form.save()
            return redirect('thankyou')
    else:
        form = HousingForm()
    return render(request,
                'myapp/Housing_create.html',
                {'form': form})

def Landlord_create(request):
    if request.method == "POST":
        request.session['user_username'] = request.user.username
        form = LandlordForm(request.POST)
        if form.is_valid():
            landlord = form.save()
            return redirect('Housing_create')
    else:
        form = LandlordForm()
    return render(request,
                'myapp/Landlord_create.html',
                {'form': form})



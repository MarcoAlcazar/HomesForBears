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
    landlord = Landlord.objects.get(pk = landlord_id)
    return render(request, 'myapp/show_landlord.html',{'landlord': landlord} )

def show_house(request, house_id):
    house = Housing.objects.get(pk = house_id)
    return render(request, 'myapp/show_house.html',{'house': house} )

def index(request):
    return render(request, 'myapp/index.html')

def create_review(request): 
    return render(request, 'myapp/create_review.html')

class apartmentss(ListView):
    template_name = 'myapp/apartmentss.html'
    model = Housing
    context_object_name = 'apartmentss'
    queryset = Housing.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Landlords'] = Landlord.objects.all()  # Add queryset for landlords to the context
        return context

def about_us(request):
   return render(request, 'myapp/about_us.html')

def review(request):
   return render(request, 'myapp/Review_create.html')

def thankyou(request):
   return render(request, 'myapp/thankyou.html')

def Housing_create(request):
    if request.method == "POST":
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
        form = LandlordForm(request.POST)
        if form.is_valid():
            landlord = form.save()
            return redirect('Housing_create')
    else:
        form = LandlordForm()
    return render(request,
                'myapp/Landlord_create.html',
                {'form': form})



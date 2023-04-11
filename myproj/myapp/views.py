from django.shortcuts import render
from django.http import HttpResponse
from .models import Landlord
from .models import Housing
from django.template import loader
from myapp.forms import LandlordForm
from myapp.forms import HousingForm
from django.shortcuts import redirect
from django.views.generic import ListView


# Create your views here.
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
        form  = HousingForm(request.POST)
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



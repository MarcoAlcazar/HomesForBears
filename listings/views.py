from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Landlord, Housing
from listings.forms import LandlordForm, HousingForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_apartments(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        apartments = Housing.objects.filter(Address__contains=searched)
        return render(request, 'listings/search_apartment.html', {'searched': searched, 'apartments': apartments})
    return render(request, 'listings/search_apartment.html')


def search_landlords(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        landlords = Landlord.objects.filter(FullName__contains=searched)
        return render(request, 'listings/search_landlords.html', {'searched': searched, 'landlords': landlords})
    return render(request, 'listings/search_landlords.html')


def show_landlord(request, landlord_id):
    landlord = get_object_or_404(Landlord, pk=landlord_id)
    return render(request, 'listings/show_landlord.html', {'landlord': landlord, 'user_username': landlord.submitted_by})


def show_house(request, house_id):
    house = get_object_or_404(Housing, pk=house_id)
    return render(request, 'listings/show_house.html', {'house': house, 'user_username': house.submitted_by})


def index(request):
    return render(request, 'listings/index.html')


def create_review(request):
    return render(request, 'listings/create_review.html')


class apartmentss(ListView):
    template_name = 'listings/apartmentss.html'
    context_object_name = 'apartmentss'
    model = Housing
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        apartment_paginator = Paginator(Housing.objects.all(), self.paginate_by)
        apartment_page = self.request.GET.get('apartment_page')
        try:
            apartments = apartment_paginator.get_page(apartment_page)
        except PageNotAnInteger:
            apartments = apartment_paginator.get_page(1)
        except EmptyPage:
            apartments = apartment_paginator.get_page(apartment_paginator.num_pages)
        context['apartments'] = apartments

        landlord_paginator = Paginator(Landlord.objects.all(), self.paginate_by)
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
    return render(request, 'listings/about_us.html')


def review(request):
    return render(request, 'listings/create_review.html')


def thankyou(request):
    return render(request, 'listings/thankyou.html')


@login_required(login_url='login')
def Housing_create(request):
    if request.method == "POST":
        form = HousingForm(request.POST, request.FILES)
        if form.is_valid():
            housing = form.save(commit=False)
            housing.submitted_by = request.user.username
            housing.save()
            return redirect('thankyou')
    else:
        form = HousingForm()
    return render(request, 'listings/Housing_create.html', {'form': form})


@login_required(login_url='login')
def Landlord_create(request):
    if request.method == "POST":
        form = LandlordForm(request.POST)
        if form.is_valid():
            landlord = form.save(commit=False)
            landlord.submitted_by = request.user.username
            landlord.save()
            return redirect('Housing_create')
    else:
        form = LandlordForm()
    return render(request, 'listings/Landlord_create.html', {'form': form})

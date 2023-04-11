from django.urls import path 

from . import views 
from myapp.views import apartmentss




urlpatterns = [
    path("", views.index, name="index"),

    path("create_review/", views.create_review, name="create_review"),

    path("apartmentss/", apartmentss.as_view(), name = "apartmentss"), 

    path("about_us/", views.about_us, name = 'about_us'),

    path("thankyou/", views.thankyou, name = 'thankyou'),

    path("Reviews/", views.review, name = 'Review_create'),

    path('landlord/add/', views.Landlord_create, name = 'Landlord_create'),

    path('housing/add/', views.Housing_create, name = 'Housing_create'),

    path('show_house/<house_id>', views.show_house, name = "show-house"),

    path('show_landlord/<landlord_id>', views.show_landlord, name = "show-landlord"),






]
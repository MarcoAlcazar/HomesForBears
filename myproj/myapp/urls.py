from django.urls import path 

from . import views 


urlpatterns = [
    path("", views.index, name="index"),

    path("create_review/", views.create_review, name="create_review"),

    path("housingg/", views.housingg, name = 'apartments'),

    path("about_us/", views.about_us, name = 'about_us'),

    path("Reviews/", views.review, name = 'Review_create'),

    path('landlord/add/', views.Landlord_create, name = 'Landlord_create'),

    path('housing/add/', views.Housing_create, name = 'Housing_create'),






]
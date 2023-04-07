from django.urls import path 

from . import views 


urlpatterns = [
    path("", views.index, name="index"),

    path("create_review/", views.create_review, name="create_review"),

    path("apartments/", views.apartments, name = 'apartments'),

    path("about_us/", views.about_us, name = 'about_us'),






]
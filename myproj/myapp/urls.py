from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.index, name="index"),

    path('<str:LandlordName>/', views.NameofLandlord, name = "Name of Landlord"), 

    path('<str:LandlordName>/LandlordReviewList/', views.LandlordReviewList, name = "Reviews"),

    path('<str:Adress>/', views.ApartmentAddress, name = "Address"),

    path('<str:Adress>/ApartmentReviewList/', views.ApartmentReviewList, name = "Reviews"),




]
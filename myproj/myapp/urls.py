from django.urls import path 

from . import views 


urlpatterns = [
    path("", views.index, name="index"),

    path("create_review/", views.create_review, name="create_review"),





]
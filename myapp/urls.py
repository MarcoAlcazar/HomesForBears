from django.urls import path 
from . import views 
from myapp.views import apartmentss
from django.contrib.auth import views as auth_views




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
    
    path('show_house/<house_id>', views.show_house, name = "show-apartment"),

    path('search_landlords', views.search_landlords, name = 'search-landlords' ),

    path('search_apartments', views.search_apartments, name = 'search-apartments' ),
    path("reset_password/", auth_views.PasswordResetView.as_view(
        template_name = "authenticate/password_reset.html"), name = "reset_password"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name = "authenticate/password_reset_done.html"), name = "password_reset_complete"),
]
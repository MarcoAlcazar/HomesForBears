from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views 
from .views import UserEditView




urlpatterns = [
   path('login_user', views.login_user, name="login"), 
   path('logout_user', views.logout_user, name = 'logout'),
   path('register_user', views.register_user, name = 'register_user'),
   path('edit_profile/', UserEditView.as_view(), name = 'edit_profile'),
   path('password/change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]
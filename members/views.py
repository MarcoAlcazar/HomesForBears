from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterUserForm, EditProfileForm
from django.views import generic
from django.shortcuts import render 
from django.urls import reverse_lazy

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


def login_user(request): 
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            messages.success(request, ('There Was An Error Logging In, Try Again...'))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request) :
    logout(request)
    messages.success(request, ("You Have Been Logged Out!"))
    return redirect('index')

def register_user(request) :
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("You Are Now Registered!"))
            return redirect('index')
    else: 
        form  = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form})


# Create your views here.

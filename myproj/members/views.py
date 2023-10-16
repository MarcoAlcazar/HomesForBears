from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

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

# Create your views here.

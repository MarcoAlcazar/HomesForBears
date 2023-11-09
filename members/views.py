from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterUserForm, EditProfileForm
from django.views import generic
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str 
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from .tokens import account_activation_token

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
            messages.success(request, ('There Was An Error Logging In, Try Again And Make Sure Your Account Is Activated (Check Your Email)...'))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request) :
    logout(request)
    messages.success(request, ("You Have Been Logged Out!"))
    return redirect('index')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user= None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for activating your account, you may now login.")
        return redirect('index')
    else:
        messages.error(request, "Activation link is invalid")
    return redirect('index')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message = render_to_string("template_activate_account.html", {
                            'user': user.username,
                            'domain': get_current_site(request).domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                            'protocol':'https' if request.is_secure() else 'http'})
    email = EmailMessage(mail_subject, message, to =[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to your email at {to_email}, and click on the recieved activation link to complete registration. Note: Check your spam folder.')
    else:
        message.error(request, f'There was an error sending email to {to_email}, check for spelling mistakes.')

def register_user(request) :
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password1']
            #user = authenticate(username = username, password = password)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')
    else: 
        form  = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form})


# Create your views here.

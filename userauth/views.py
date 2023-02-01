from django.shortcuts import render, redirect
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauth.models import User

# User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}, your account created successfully')
            new_user = authenticate(username= form.cleaned_data['email'],
                                    password = form.cleaned_data['password1']
                                    )
            login(request, new_user)
            return redirect('core:home')
    else:
        form = UserRegisterForm(request.POST or None)
    
    context = {'form': form}
    return render(request, 'userauth/register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password= password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in')
                return redirect('core:home')
            else:
                messages.warning(request, 'Email or password wrong! Please enter valid email and password')
        except:
            messages.warning(request, f'User with {email} dose not exist')
            
    
    return render(request, 'userauth/sign-in.html')

def logout_view(request):
    messages.success(request, 'You are logged out!')
    logout(request)
    return redirect('userauth:sign-in')
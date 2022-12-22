from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def login(request):
    auth.logout(request)
    return render(request, 'login.html')

def signin(request):
    if request.method != 'POST':
        return redirect('login')
    
    email = request.POST.get('email').strip()
    password = request.POST.get('password')

    if len(password) == 0 or len(email) == 0:
        messages.add_message(request, constants.ERROR, 'Please, enter a valid email and password.')
        return redirect('login')

    try:
        username = User.objects.get(email=email.lower()).username
    except:
        username = None
    
    if not username:
        messages.add_message(request, constants.ERROR, 'Email not found.')
        return redirect('login')

    user = authenticate(username=username, password=password)
    if not user:
        messages.add_message(request, constants.ERROR, 'Invalid email or password.')
        return redirect('login') 
    else:
        auth.login(request, user)
        messages.add_message(request, constants.SUCCESS, f'Sign-in sucessfull! Welcome {user.first_name}!')
        return redirect('secure')

def register(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method != 'POST':
        return redirect('register')

    name = request.POST.get('name')
    email = request.POST.get('email').strip()
    password = request.POST.get('password').strip()
    confirm_password = request.POST.get('confirm_password').strip()

    if len(password) == 0 or len(email) == 0:
        messages.add_message(request, constants.ERROR, 'Please, enter a valid email and password.')
        return redirect('register')
    elif password != confirm_password:
        messages.add_message(request, constants.ERROR, 'The password confirmation doesn\'t match.')
        return redirect('register')
    elif User.objects.filter(email = email).exists():
        messages.add_message(request, constants.ERROR, 'A user with that email already exists.')
        return redirect('register')

    try:
        [first_name, last_name] = name.split(' ', 1)

        user = User.objects.create_user(
            first_name = first_name.strip(), 
            last_name = last_name.strip(), 
            username = email.split('@', 1)[0],
            email = email, 
            password = password
        )
        user.save()

        messages.add_message(request, constants.SUCCESS, 'Sign-up sucessfull!')
        return redirect('login')
    except:
        messages.add_message(request, constants.ERROR, 'Error registering user! Please try again.')
        return redirect('register')

def logout(request):
    auth.logout(request)
    messages.clear()
    return redirect('welcome')

@login_required(login_url='login')
def secure(request):
    user = request.user
    logout_path = reverse('logout')
    return HttpResponse(f'You are logged in as {user.first_name}. <a href="{logout_path}">Logout</a>')

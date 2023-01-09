from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives, send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

token_generator = PasswordResetTokenGenerator()

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

    try:
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

        first_name, *last_name = name.split(' ', 1)
        last_name = last_name[0] if last_name else ''

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
    return redirect('welcome')

@login_required(login_url='login')
def secure(request):
    user = request.user
    logout_path = reverse('logout')
    return HttpResponse(f'You are logged in as {user.first_name}. <a href="{logout_path}">Logout</a>')

def password_reset(request):
    # if request by GET method only show the reset page
    if request.method != 'POST':
        return render(request, 'password_reset/reset.html')

    try:
        email = request.POST.get('email').strip()
        user = User.objects.get(email=email.lower())
    except:
        user = None

    if not user:
        messages.add_message(request, constants.ERROR, 'Email not found.')
        return redirect('password_reset')

    token = token_generator.make_token(user)
    url_to_reset = request.build_absolute_uri(reverse('password_reset_confirm', kwargs={'id': user.id, 'token': token}))
    html_message = render_to_string('password_reset/email_reset.html', {'url': url_to_reset})
    text_message = strip_tags(html_message)

    email = EmailMultiAlternatives(
        'Password Reset',
        text_message,
        settings.EMAIL_FROM_ADDRESS,
        [user.email], 
    )
    email.attach_alternative(html_message, "text/html")
    email.send()

    return redirect('password_reset_done')

def password_reset_done(request):
    return render(request, 'password_reset/reset_done.html')

def password_reset_confirm(request, id, token):
    try:
        user = User.objects.get(pk=id)
    except:
        messages.add_message(request, constants.ERROR, 'User not found.')
        return redirect('password_reset')

    is_valid = token_generator.check_token(user, token)
    if not is_valid:
        messages.add_message(request, constants.ERROR, 'Invalid token.')
        return redirect('password_reset')

    if request.method == 'GET':
        return render(request, 'password_reset/reset_confirm.html')
    else:
        password = request.POST.get('password').strip()
        confirm_password = request.POST.get('confirm_password').strip()

        if len(password) == 0:
            messages.add_message(request, constants.ERROR, 'Please, enter a valid password.')
            return render(request, 'password_reset/reset_confirm.html')
        elif not password == confirm_password:
            messages.add_message(request, constants.ERROR, 'Password does not match.')
            return render(request, 'password_reset/reset_confirm.html')

        user.set_password(password)
        user.save()

        messages.add_message(request, constants.SUCCESS, 'Password has been changed successfully!')
        return redirect('login')


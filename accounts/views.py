# accounts/views.py
import jwt
import requests

from .models import Profile
from .forms import SignUpForm
from django.conf import settings
from django.db import transaction
from urllib.parse import urlencode
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def linkedin_login(request):
    params = {
        'response_type': 'code',
        'client_id': settings.LINKEDIN_CLIENT_ID,
        'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
        'scope': 'profile email openid'
    }
    url = 'https://www.linkedin.com/oauth/v2/authorization?' + urlencode(params)
    return redirect(url)

def linkedin_callback(request):
    code = request.GET.get('code')
    if code:
        params = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
            'client_id': settings.LINKEDIN_CLIENT_ID,
            'client_secret': settings.LINKEDIN_CLIENT_SECRET,
        }
        response = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data=params)
        access_token = response.json().get('access_token')
        id_token = response.json().get('id_token')  # Extract the ID token

        if not access_token or not id_token:
            return render(request, 'accounts/login.html', {'error': 'Authentication failed'})

        decoded_id_token = jwt.decode(id_token, options={"verify_signature": False})
        email = decoded_id_token.get('email')
        given_name = decoded_id_token.get('given_name')
        family_name = decoded_id_token.get('family_name')
        name = decoded_id_token.get('name')
        picture = decoded_id_token.get('picture')
        locale = decoded_id_token.get('locale')

        with transaction.atomic():
            user, created = User.objects.get_or_create(username=email, defaults={'first_name': given_name, 'last_name': family_name, 'email': email})
            if created:
                profile = Profile.objects.create(user=user, name=name, email=email, locale=locale, linkedin_photo_url=picture)
                profile.download_linkedin_photo()
            else:
                user.first_name = given_name
                user.last_name = family_name
                user.email = email
                user.save()
                profile = Profile.objects.get(user=user)
                profile.name = name
                profile.email = email
                profile.locale = locale
                profile.linkedin_photo_url = picture
                profile.save()
                if not profile.profile_photo:
                    profile.download_linkedin_photo()

        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html', {'error': 'Authentication failed'})

def logout_view(request):
    return render(request, 'accounts/logout.html')

def logout_confirm_view(request):
    logout(request)
    return redirect('login')

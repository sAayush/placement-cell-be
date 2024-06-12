import jwt
import requests

from .models import Profile
from django.conf import settings
from django.db import transaction
from urllib.parse import urlencode
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login_view(request):

    return render(request, 'accounts/login.html')


def linkedin_login(request):
    params = {
        'response_type': 'code',
        'client_id': settings.LINKEDIN_CLIENT_ID,
        'redirect_uri': settings.LINKEDIN_REDIRECT_URI,
        'scope': 'profile email openid'
        # 'state': 'DCEeFWf45A53sdfKef424',  # Example state value
    }
    url = 'https://www.linkedin.com/oauth/v2/authorization?' + \
        urlencode(params)
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
        response = requests.post(
            'https://www.linkedin.com/oauth/v2/accessToken', data=params)
        access_token = response.json().get('access_token')
        id_token = response.json().get('id_token')  # Extract the ID token

        if not access_token or not id_token:
            print('No access token found in response')

        print('access_token:', access_token)
        print('id_token:', id_token)

        decoded_id_token = jwt.decode(
            id_token, options={"verify_signature": False})

        sub = decoded_id_token.get('sub')
        name = decoded_id_token.get('name')
        given_name = decoded_id_token.get('given_name')
        family_name = decoded_id_token.get('family_name')
        email = decoded_id_token.get('email')
        picture = decoded_id_token.get('picture')

        print('decoded_id_token:', decoded_id_token)
        print('sub:', sub)
        print('name:', name)
        print('given_name:', given_name)
        print('family_name:', family_name)
        print('email:', email)
        print('picture:', picture)

        # Fetch user profile information from LinkedIn
        userinfo_response = requests.get(
            'https://api.linkedin.com/v2/userinfo',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        userinfo_data = userinfo_response.json()
        locale = userinfo_data.get('locale')

        print('userinfo_data:', userinfo_data)
        print('locale:', locale)

        # Create or update user in the database
        with transaction.atomic():

            profile, _ = Profile.objects.get_or_create(email=email)
            profile.name = name
            profile.email = email
            profile.locale = locale
            # profile.headline = headline
            profile.picture = picture
            profile.save()

        return redirect('home')

    return render(request, 'accounts/login.html', {'error': 'Authentication failed'})

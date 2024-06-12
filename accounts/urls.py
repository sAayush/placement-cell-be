from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('linkedin/', linkedin_login, name='linkedin_login'),
    path('linkedin/callback/', linkedin_callback, name='linkedin_callback'),
]

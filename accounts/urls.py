from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('linkedin/', linkedin_login, name='linkedin_login'),
    path('linkedin/callback/', linkedin_callback, name='linkedin_callback'),
    path('logout/', logout_view, name='logout'),
    path('logout_confirm/', logout_confirm_view, name='logout_confirm'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),

]

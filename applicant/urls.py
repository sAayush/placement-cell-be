from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('profile/', views.profile, name='profile-page'),
    # path('login/', views.LoginView.as_view(template_name='applicant/login.html'), name='login'),
    # path('logout/', views.LogoutView.as_view(template_name='applicant/logout.html'), name='logout'),

]
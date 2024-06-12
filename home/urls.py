from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('profile/', profile_view, name='profile'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

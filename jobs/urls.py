from django.urls import path
from .views import *

urlpatterns = [
    path('post-job/', JobPostCreateView.as_view(), name='post-job'),
    path('jobs/', JobListView.as_view(), name='jobs-list'),
]

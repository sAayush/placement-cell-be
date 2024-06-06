from django.db import models
from django.contrib.auth.models import User

import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    locale = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def color_code(self):
        random.seed(self.user.username)
        return ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


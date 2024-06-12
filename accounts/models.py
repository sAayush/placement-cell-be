from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username  # Correctly reference the user attribute

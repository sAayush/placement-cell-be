from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    # headline = models.CharField(max_length=255, blank=True, null=True)
    picture = models.URLField(blank=True, null=True)  # To store the profile picture URL

    def __str__(self):
        return self.user.username

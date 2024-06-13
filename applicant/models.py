from django.db import models
from django.contrib.auth import get_user_model
# # Create your models here.

User=get_user_model()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    about=models.CharField(max_length=250, null=True, blank=True)
    education=models.CharField(max_length=250, null=True, blank=True)
    certification=models.CharField(max_length=250, null=True, blank=True)
    experience=models.CharField(max_length=250, null=True, blank=True)
    tech_stack=models.CharField(max_length=250, null=True, blank=True)
    project=models.CharField(max_length=250, null=True, blank=True)
    

    def __str__(self):
        return self.user.username
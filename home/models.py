from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


class Education(models.Model):
    class EducationLevel(models.TextChoices):
        SSC = 'SSC', 'SSC'
        HSC = 'HSC', 'HSC'
        BACHELORS = 'Bachelors', 'Bachelors'
        MASTERS = 'Masters', 'Masters'
        PHD = 'PhD', 'PhD'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    level = models.CharField(max_length=20, choices=EducationLevel.choices)
    marks_or_cgpa = models.FloatField()
    year_of_passing = models.DateField()
    board_or_university = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, null=True, blank=True)
    
class AdditionalInfo(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='additional_info')
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Additional Info for {self.profile.user.username}"

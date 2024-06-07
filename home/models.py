# home/models.py
from django.db import models
from accounts.models import Profile

class Education(models.Model):
    class EducationLevel(models.TextChoices):
        SSC = '10th', 'SSC'
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

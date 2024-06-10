# home/models.py
from django.db import models
from accounts.models import Profile

class Education(models.Model):
    class EducationLevel(models.TextChoices):
        TENTH = '10th', '10th'
        TWELFTH = '12th', '12th'
        BACHELORS = 'Bachelors', 'Bachelors'
        MASTERS = 'Masters', 'Masters'
        PHD = 'PhD', 'PhD'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    level = models.CharField(max_length=20, choices=EducationLevel.choices)
    marks_or_cgpa = models.FloatField()
    year_of_passing = models.DateField()
    board_or_university = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.degree + ' - ' + self.profile.name
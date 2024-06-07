# home/forms.py
from django import forms
from accounts.models import Profile
from .models import Education

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'locale', 'headline', 'profile_photo', 'date_of_birth', 'address', 'phone_number']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['level', 'marks_or_cgpa', 'year_of_passing', 'board_or_university', 'degree']

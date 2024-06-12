# home/forms.py
from django import forms
from accounts.models import Profile
from .models import Education


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'locale', 'headline',
                  'profile_photo', 'date_of_birth', 'address', 'phone_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['level', 'marks_or_cgpa', 'year_of_passing',
                  'board_or_university', 'degree']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'marks_or_cgpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'year_of_passing': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'board_or_university': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
        }

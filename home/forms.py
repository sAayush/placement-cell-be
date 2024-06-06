from django import forms
from django.contrib.auth.models import User
from .models import Profile, Education, AdditionalInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'locale', 'date_of_birth', 'address', 'education', 'experience']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['level', 'marks_or_cgpa', 'year_of_passing', 'board_or_university', 'degree']
        
class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        fields = ['address', 'phone_number', 'date_of_birth', 'additional_info']
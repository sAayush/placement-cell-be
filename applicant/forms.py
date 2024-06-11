# profiles/forms.py
from django import forms
from .models import UserProfile

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['education', 'certification', 'experience', 'tech_stack', 'project']
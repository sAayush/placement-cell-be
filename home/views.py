# home/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Education
from .forms import ProfileForm, EducationForm
from django.forms import modelformset_factory

@login_required
def home_view(request):
    return render(request, 'home/home.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1)
        education_formset = EducationFormSet(request.POST, queryset=request.user.profile.educations.all())
        
        if profile_form.is_valid() and education_formset.is_valid():
            profile_form.save()
            education_formset.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1)
        education_formset = EducationFormSet(queryset=request.user.profile.educations.all())

    return render(request, 'home/profile.html', {
        'profile_form': profile_form,
        'education_formset': education_formset,
    })

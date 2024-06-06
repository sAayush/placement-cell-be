from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Education, AdditionalInfo
from .forms import UserForm, ProfileForm, EducationForm, AdditionalInfoForm
from django.forms import modelformset_factory

@login_required
def home_view(request):
    return render(request, 'home/home.html')

@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        additional_info_form = AdditionalInfoForm(request.POST, instance=request.user.profile.additional_info)
        
        if profile_form.is_valid() and additional_info_form.is_valid():
            profile_form.save()
            additional_info_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        additional_info_form = AdditionalInfoForm(instance=request.user.profile.additional_info)
        EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1)

    return render(request, 'home/profile.html', {
        'profile_form': profile_form,
        'education_formset': EducationFormSet(queryset=request.user.profile.educations.all()),
        'additional_info_form': additional_info_form
})

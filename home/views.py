# home/views.py
from xhtml2pdf import pisa
from .models import Education
# Import custom user model if necessary
from accounts.models import CustomUser, Profile
from django.http import HttpResponse
from django.forms import modelformset_factory
from .forms import ProfileForm, EducationForm
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    return render(request, 'home/home.html')


@login_required
def profile_view(request):
    EducationFormSet = modelformset_factory(
        Education, form=EducationForm, extra=1, can_delete=True)
    profile_form = ProfileForm(
        request.POST or None, request.FILES or None, instance=request.user.profile)
    education_formset = EducationFormSet(
        request.POST or None, queryset=request.user.profile.educations.all())

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile')
        elif 'education_submit' in request.POST:
            if education_formset.is_valid():
                for form in education_formset:
                    education = form.save(commit=False)
                    education.profile = request.user.profile
                    education.save()
                return redirect('profile')

    return render(request, 'home/profile.html', {
        'profile_form': profile_form,
        'education_formset': education_formset,
    })


@login_required
def generate_pdf(request):
    html_string = render_to_string(
        'home/user_information.html', {'user': request.user})
    pdf = HttpResponse(content_type='application/pdf')
    pdf['Content-Disposition'] = 'attachment; filename="Profile_Information.pdf"'
    pisa.CreatePDF(html_string, dest=pdf)
    return pdf

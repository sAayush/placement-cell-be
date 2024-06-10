# home/views.py
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.http import HttpResponse
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
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1, can_delete=True)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        education_formset = EducationFormSet(request.POST, queryset=request.user.profile.educations.all())
        
        if profile_form.is_valid() and education_formset.is_valid():
            profile_form.save()
            for form in education_formset:
                education = form.save(commit=False)
                education.profile = request.user.profile
                education.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1)
        education_formset = EducationFormSet(queryset=request.user.profile.educations.all())

    return render(request, 'home/profile.html', {
        'profile_form': profile_form,
        'education_formset': education_formset,
    })

def generate_pdf(request):
     # Render HTML template to string
    html_string = render_to_string('home/user_information.html', {'user': request.user})

    # Generate PDF from HTML string
    pdf = HttpResponse(content_type='application/pdf')
    pdf['Content-Disposition'] = 'attachment; filename="Profile_Information.pdf"'

    # Create PDF
    pisa.CreatePDF(html_string, dest=pdf)

    return pdf
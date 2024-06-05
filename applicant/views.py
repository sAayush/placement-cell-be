from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'applicant/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UserRegisterForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = UserRegisterForm(instance=request.user.profile)
    
    context = {
        'p_form': p_form
    }
    return render(request, 'applicant/profile.html', context)
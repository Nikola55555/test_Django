from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import UserRegistrationForm
from django.contrib import messages


def index(request):
    return render(request, 'site_app/base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created! You are now able to')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages
from users.forms import CustomUserCreationForm

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {"form": CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, "Error")
            return render(request, 'register.html', {"form": CustomUserCreationForm})
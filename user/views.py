from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, ProfileForm
from .models import Profile
# Create your views here.


def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('Customer:profile_update')
        else:
            form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username or password incorrect')
    return render(request, 'login.html')


def logout_form(request):
    logout(request)
    return redirect('Customer:login')


def userprofile(request):
    user = request.user
    print(user)
    profile = get_object_or_404(Profile, user=user)
    print(profile.first_name)
    print(profile.last_name)
    print(profile.email)
    return render(request, 'profile.html', {'profile': profile})


def profile_form(request, pk=None):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profileedit.html', {'form': form})
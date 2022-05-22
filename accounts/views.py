from django.shortcuts import render


# Create your views here.


def login_function(request):
    return render(request,'accounts/login.html',{})

def profile_function(request):
    return render(request,'accounts/profile.html',{})

def register_function(request):
    return render(request,'accounts/register.html',{})

def profiles_function(request):
    return render(request,'accounts/profiles.html',{})

def dashboard_function(request):
    return render(request,'accounts/dashboard.html',{})

def create_profile_function(request):
    return render(request,'accounts/create-profile.html',{})

def add_education_function(request):
    return render(request,'accounts/add-education.html',{})

def add_experience_function(request):
    return render(request,'accounts/add-experience.html',{})
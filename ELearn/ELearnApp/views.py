from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def register(request):
    return render(request, 'register.html') 

def login(request):
    return render(request, 'login.html') 
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return render(request, 'homepage/home.html', {})
    return render(request, 'homepage/stunning.html', {})


def secret(request):
    return render(request, 'homepage/secret_home.html', {})
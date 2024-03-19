from django.shortcuts import render
from .models import Notes


def home(request):
    context = {
        'notes': Notes.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'О магазине PROASS'})
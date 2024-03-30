from django.shortcuts import render
from .models import Notes
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title': 'О магазине PROASS'})

@login_required
def notes(request):
    context = {
        'notes': Notes.objects.filter(author=request.user)
    }
    return render(request, 'my_notes.html', context)
from django.shortcuts import render
from .models import Services, Achievements, About


def homepage(request):
    services = Services.objects.all()
    achievements = Achievements.objects.all()
    context = {
        'services' : services,
        'achievements': achievements,
    }
    return render(request, 'html/home.html', context)

def aboutus(request):
    intro = About.objects.first()
    achievements = Achievements.objects.all()  # Fetch achievements data
    context = {
        'about': intro,
        'achievements': achievements,
    }
    return render(request, 'html/aboutus.html', context)

from django.shortcuts import render, HttpResponse
from .models import Person

# Create your views here.


def indexPageView(request):
    return render(request, 'traffickingapp/index.html')


def victimsPageView(request):
    db_people = Person.objects.all()
    context = {
        "people": db_people
    }
    return render(request, 'traffickingapp/victims.html', context)


def helpPageView(request):
    return render(request, 'traffickingapp/help.html')

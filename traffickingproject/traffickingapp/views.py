from django.shortcuts import render, HttpResponse
from .models import Person

# Create your views here.


def indexPageView(request):
    return render(request, 'traffickingapp/index.html')


def victimsPageView(request):
    try: 
        first_name = request.GET['firstName']
        
        people = Person.objects.filter(first_name=first_name) 

    except: 
        people = Person.objects.all()
    
    db_people = Person.objects.all()
    context = {
        "people": db_people
    }
    return render(request, 'traffickingapp/victims.html', context)


def helpPageView(request):
    return render(request, 'traffickingapp/help.html')

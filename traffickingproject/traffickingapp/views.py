from django.shortcuts import render, HttpResponse
from .models import Person

# Create your views here.


def indexPageView(request):
    return render(request, 'traffickingapp/index.html')


def victimsPageView(request):
    try: 
        fName = request.GET['first_name']
        
        people = Person.objects.filter(first_name=fName) 

    except: 
        people = Person.objects.all()
    
    context = {
        "people": people
    }
    return render(request, 'traffickingapp/victims.html', context)

# def searchPageView(Request): 
#     fName = request.GET['first_name'] 

#     return render(request)


def helpPageView(request):
    return render(request, 'traffickingapp/help.html')

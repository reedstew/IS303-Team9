from django.shortcuts import render, HttpResponse, redirect
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


def searchPageView(request):
    try:
        fName = request.GET['first_name']

        people = Person.objects.filter(first_name=fName)

    except:
        people = Person.objects.all()

    context = {
        "people": people
    }
    return render(request, 'traffickingapp/victims.html', context)


def addPageView(request):
    if request.method == 'POST':
        # Add in a new person
        # Get first_name, last_name, age_at_missing, city, state, gender, race
        date_missing = request.POST['date_missing']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age_at_missing = request.POST['age_at_missing']
        city = request.POST['city']
        state = request.POST['state']
        gender = request.POST['gender']
        race = request.POST['race']
        # Create a book

        new_person = Person()

        new_person.date_missing = date_missing
        new_person.first_name = first_name
        new_person.last_name = last_name
        new_person.age_at_missing = age_at_missing
        new_person.city = city
        new_person.state = state
        new_person.gender = gender
        new_person.race = race

        new_person.save()

        return redirect('index')
    else:
        people = Person.objects.all()

        context = {
            "people": people
        }

        return render(request, "traffickingapp/add.html", context)


def helpPageView(request):
    return render(request, 'traffickingapp/help.html')

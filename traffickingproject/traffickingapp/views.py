from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPageView(request):
    return render(request, 'traffickingapp/index.html')


def victimsPageView(request):
    return render(request, 'traffickingapp/victims.html')


def helpPageView(request):
    return render(request, 'traffickingapp/help.html')

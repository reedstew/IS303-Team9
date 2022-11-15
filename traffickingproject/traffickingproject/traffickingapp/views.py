from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPageView(request):
    return HttpResponse('Human Trafficking in Utah')

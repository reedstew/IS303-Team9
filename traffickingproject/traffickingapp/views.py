from django.shortcuts import render, HttpResponse

# Create your views here.


def indexPageView(request):
    return render(request, 'traffickingapp/index.html')

from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'template/base.html')

def trialPage(request):
    return render(request, 'template/trial1.html')
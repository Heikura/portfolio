from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'homepage/index.html')

def cv(request):
    return render(request, 'homepage/cv.html')

def contact(request):
    return render(request, 'homepage/contact.html')

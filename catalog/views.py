from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'catalog/index.html') 

def about(request):
    return render(request, 'catalog/about.html')

def mission(request):
    return render(request, 'catalog/mission.html')

def booklist(request):
    return render(request, 'catalog/booklist.html')

def checkout(request):
    return render(request, 'catalog/checkout.html')

def register(request):
    return render(request, 'catalog/register.html')
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/index.html')
    #return HttpResponse('Minha primeira view')

def about(request):
    return render(request, 'core/about.html')

def speaker(request):
    return render(request, 'core/speakers.html')

def event(request):
    return render(request, 'core/events.html')

def new(request):
    return render(request, 'core/news.html')

def contact(requers):
    return render(requers, 'core/contact.html')
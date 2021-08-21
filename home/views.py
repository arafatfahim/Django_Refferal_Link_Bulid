from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('Welcome')
    return render (request, 'home/home.html')
def about(request):
    return render (request, 'home/about.html')
def contact(request):
    return render (request, 'home/contact.html')
def project(request):
    return render (request, 'home/projects.html')
def cv(request):
    return render (request, 'home/cv.html')
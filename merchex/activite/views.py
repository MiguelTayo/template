from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def bienvenue(request):
    return HttpResponse('<h1> <center>Bienvenue à vous! <center> </h1>')

def index (request):
    return render (request, 'activite/index.html')

def about (request):
    return render (request, 'activite/about.html')    

def project (request):
    return render (request, 'activite/project.html')   

    
def staff (request):
    return render (request, 'activite/staff.html')   

def contact (request):
    return render (request, 'activite/contact.html')             
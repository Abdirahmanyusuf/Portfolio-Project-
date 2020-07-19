from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    profiles = profile.objects.all()
    skill = skills.objects.all()
    clients = client.objects.all()
    portifolio = portfolio.objects.all()[:3]
    context = {'profiles': profiles, 'skill': skill,
               'clients': clients, 'portifolio': portifolio}
    return render(request, 'portifolio/index.html', context)


def about(request):

    context = {}
    return render(request, 'portifolio/about.html', context)


def contact(request):
    context = {}
    return render(request,  'portifolio/contact.html')


def Cv(request):
    context = {}
    return render(request,  'portifolio/Cv.html')


def project(request):
    portifolio = portfolio.objects.all()
    context = {'portifolio': portifolio}
    return render(request,  'portifolio/project.html', context)

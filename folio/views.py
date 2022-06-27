from django.shortcuts import render
from .models import *

# Create your views here.
def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    projects = Projects.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "projects": projects,
    }
    return render(request, 'index.html', context)


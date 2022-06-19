from django.shortcuts import render
from .models import about
from .models import slider
from .models import client
from .models import service6

# Create your views here.
def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    service6data = service6.objects.all()[1]
    context = {
    'about': aboutdata,
    'slider': sliderdata,
    'client': clientdata,
    'service6': service6data
    }
    return render(request,'index.html',context)
def aboutus(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def projects(request):
    return render(request,'projects.html')

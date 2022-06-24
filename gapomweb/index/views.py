from django.shortcuts import render
from .models import about
from .models import slider
from .models import client
from .models import projectview
from .models import mega67

# Create your views here.
def home(request):
    aboutdata = about.objects.all()[0]
    sliderdata = slider.objects.all()
    clientdata = client.objects.all()
    projectviewdata = projectview.objects.all()
    mega67data = mega67.objects.all()
    context = {
    'about': aboutdata,
    'slider': sliderdata,
    'client': clientdata,
    'projectview': projectviewdata,
    'mega67': mega67data
    }
    return render(request,'index.html',context)

def projects(request):
    return render(request,'projects.html')

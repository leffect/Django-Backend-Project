from django.shortcuts import render
from .models import aboutcontent

# Create your views here.
def aboutinfo(request):
    aboutcontentdata = aboutcontent.objects.all()
    context = {
    'aboutcontent': aboutcontentdata
    }
    return render(request,'about.html',context)

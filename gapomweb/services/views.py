from django.shortcuts import render
from .models import serve77

# Create your views here.
def services(request):
    serve77data = serve77.objects.all()
    context = {
        'serve77': serve77data,
}

    return render(request,'services.html',context)

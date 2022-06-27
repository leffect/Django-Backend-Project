from django.shortcuts import render
from .models import projectile

# Create your views here.
def projects(request):
    projectiledata = projectile.objects.all()
    context = {
        'projectile': projectiledata
}
    return render(request,'projects.html',context)

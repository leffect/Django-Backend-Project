from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.aboutus, name='about'),
    path('services/',views.services,name='services'),
    path('projects/',views.projects,name='projects'),
]

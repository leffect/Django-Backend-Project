from django.urls import path
from . import views

urlpatterns = [
    path('',views.aboutinfo, name='about'),
]

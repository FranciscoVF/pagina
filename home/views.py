from django.shortcuts import render
from django.views import generic
# Create your views here.

from .models import Cundina

class Home(generic.ListView):
    template_name = "paginas/home.html"
    model = Cundina

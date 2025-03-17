from django.shortcuts import render
from .models import Genero

def index(request):
    return render(request, 'blog/index.html')

def generos_list(request):
    generos = Genero.objects.all()
    return render(request, 'blog/pelis_list.html', {'generos': generos})

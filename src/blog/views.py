from django.shortcuts import render
from .models import Genero, Pelicula, Resena

def index(request):
    generos = Genero.objects.all()
    peliculas = Pelicula.objects.all()
    resenas = Resena.objects.all()  

    return render(request, 'blog/index.html', {  
        'generos': generos,  
        'peliculas': peliculas,  
        'resenas': resenas 
    })

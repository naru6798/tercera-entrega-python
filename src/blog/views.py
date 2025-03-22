from django.shortcuts import render, redirect
from .models import Genero, Pelicula, Resena
from . import models, forms
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy

def index(request):
    generos = Genero.objects.all()
    peliculas = Pelicula.objects.all()
    resenas = Resena.objects.all()  

    if request.method == 'POST':
        form = forms.ResenaForm(request.POST)
        if form.is_valid():
            nueva_resena = form.save(commit=False)
            pelicula_id = request.POST.get('pelicula_id')
            try:
                nueva_resena.pelicula = models.Pelicula.objects.get(id=pelicula_id)
                nueva_resena.save()
                return redirect('blog:index')
            except models.Pelicula.DoesNotExist:
                return render(request, 'blog/index.html', {  
                'generos': generos,  
                'peliculas': peliculas,  
                'resenas': resenas, 
                'form': form,
                'error': "La película seleccionada no existe en la página aun."
    })
    else:
        form = forms.ResenaForm()



    return render(request, 'blog/index.html', {  
        'generos': generos,  
        'peliculas': peliculas,  
        'resenas': resenas, 
        'form': form
    })

def proximos_estrenos(request):
    return render(request, 'blog/proximos-estrenos.html')

def resena_update(request, pk):
    query = models.Resena.objects.get(id=pk)
    if request.method == "GET":
        form = forms.ResenaForm(instance=query)
    if request.method == "POST":
        form = forms.ResenaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    return render(request, 'blog/resena_update.html', {'form': form})

def resena_delete(request, pk):
    query = models.Resena.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect('blog:index')
    return render(request, 'blog/resena_delete.html', {'query': query})

class MiLoginView(LoginView):
    template_name = 'blog/login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('blog:index')

def buscar(request):
    busqueda = request.GET.get('busqueda')

    if busqueda:
        peliculas = Pelicula.objects.filter(titulo__icontains=busqueda)
    else:
        peliculas = Pelicula.objects.all()
    
    return render(request, 'blog/buscar.html', {'peliculas': peliculas})

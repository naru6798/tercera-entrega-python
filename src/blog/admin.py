from django.contrib import admin

from . import models

admin.site.register(models.Genero)
#admin.site.register(models.Pelicula) Lo saco porque lo estoy registrando abajo
admin.site.register(models.Resena)

@admin.register(models.Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'director', 'fecha_estreno')
    search_fields = ('titulo', 'director', 'genero')
    list_filter = ('genero', 'director', 'fecha_estreno')
    ordering = ('titulo', 'fecha_estreno', 'genero')
    
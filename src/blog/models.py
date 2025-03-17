from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    director = models.CharField(max_length=100)
    fecha_estreno = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
    

class Resena(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    autor = models.CharField(max_length=100, null=True, blank = True)
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.pelicula.titulo} por {self.autor}"
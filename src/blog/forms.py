from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['puntuacion', 'autor', 'comentario']
        widgets = {
            'puntuacion': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'autor': forms.TextInput(attrs={'placeholder': 'Nombre del autor'}),
            'comentario': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu reseña aqui...'})
        }

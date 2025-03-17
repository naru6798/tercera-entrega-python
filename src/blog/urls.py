from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.proximos_estrenos, name='proximos-estrenos'),
    path('index/', views.index, name='index')
]
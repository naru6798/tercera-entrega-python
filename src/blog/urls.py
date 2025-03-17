from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('proximos-estrenos/', views.proximos_estrenos, name='proximos-estrenos'),
]
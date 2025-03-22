from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('proximos-estrenos/', views.proximos_estrenos, name='proximos-estrenos'),
    path('resena-update/<int:pk>/', views.resena_update, name='resena_update'),
    path('resena-delete/<int:pk>/', views.resena_delete, name='resena_delete'),
]
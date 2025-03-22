from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('proximos-estrenos/', views.proximos_estrenos, name='proximos-estrenos'),
    path('resena-update/<int:pk>/', views.resena_update, name='resena_update'),
    path('resena-delete/<int:pk>/', views.resena_delete, name='resena_delete'),
    path('login/', views.MiLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('buscar/', views.buscar, name='buscar')
]
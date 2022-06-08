from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('Aplicaciones.ModeloInicio.urls'), name="inicio_urls"),
    path('', include('Aplicaciones.ModuloUsuario.urls'), name="usuarios_urls"),
    path('', include('Aplicaciones.ModuloTickets.urls'), name="tickets_urls"),
]

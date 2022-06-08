from django.urls import path
from Aplicaciones.ModeloInicio.views import inicio, menu, mision, contacto



urlpatterns = [
    path('', inicio, name="inicio"),
    path('menu', menu, name="menu"),
    path('mision', mision, name="mision"),
    path('contacto', contacto, name="contacto"),
]
from unicodedata import name
from django.urls import path
from Aplicaciones.ModuloUsuario.views import inicio,formregistro, editarUsuario,borrarUsuario


urlpatterns = [
    path('usuario', inicio, name="inicioU"),
    path('formregistro', formregistro, name="formregistro"),
    path('editarUsuario/<int:id>', editarUsuario ,name="editarUsuario"),
    path('borrarUsuario/<int:id>', borrarUsuario  ,name="borrarUsuario")
]
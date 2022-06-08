from unicodedata import name
from django.urls import path
from Aplicaciones.ModuloTickets.views import inicio, formrtickets,editarticket,borrarticket 


urlpatterns = [
    path('tickets', inicio, name="inicio"),
    path('formrtickets', formrtickets, name="formrtickets"),
    path('editarticket/<int:id>', editarticket ,name="editarticket"),
    path('borrarticket/<int:id>', borrarticket ,name="borrarticket"),
    
]
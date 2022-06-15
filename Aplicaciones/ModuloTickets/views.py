from django.shortcuts import  redirect, render
from .models import tickets, Ciudades, Tarifas, Horario, ModulousuarioUsuario, Vehiculos
from .forms import ticketsForm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create your views here.
def inicio(request):
     ticket = tickets.objects.raw('SELECT vh.marca, vh.placa, u.nombre , t.id, c.ciudad, cd.ciudadD, h.hora_salida, ta.precios FROM vehiculos as vh,  modulousuario_usuario as u, modulotickets_tickets as t, ciudades as c, ciudadesd as cd, horario as h, tarifas as ta where vh.id = t.bus AND u.id = t.nombre AND c.id = t.inicio  AND cd.id = t.destino AND h.id = t.horario AND ta.id = t.tarifa')
     dicTIC = {
          'tickets': ticket
     }
     return render(request, "TicketsHTMLS/tickets.html", dicTIC)


def formrtickets(request):
     ciudad = Ciudades.objects.all()
     tarifas = Tarifas.objects.all() 
     horario = Horario.objects.all() 
     usuario = ModulousuarioUsuario.objects.all()
     vehiculo = Vehiculos.objects.all()
     if(request.method == 'GET'):
          forms = ticketsForm()
          dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario,
            'usuario':usuario,
            'vehiculo': vehiculo  
          }
     else:
         forms = ticketsForm(request.POST)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario,
            'usuario':usuario,
            'vehiculo': vehiculo   
          }
         print(dicformTIC['usuario'])
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
     return render(request, 'TicketsHTMLS/formtickets.html',dicformTIC)


def editarticket(request , id):
    ciudad = Ciudades.objects.all()
    tarifas = Tarifas.objects.all()
    horario = Horario.objects.all() 
    usuario = ModulousuarioUsuario.objects.all()
    vehiculo = Vehiculos.objects.all()
    ticket = tickets.objects.get(id = id)
    if(request.method == 'GET'):
       forms = ticketsForm(instance = ticket)
       dicformTIC ={
              'form': forms,
              'ciudad':ciudad,
              'tarifas':tarifas,
              'horario':horario,
              'usuario':usuario,
              'vehiculo': vehiculo
         } 
    else:
         forms = ticketsForm(request.POST, instance = ticket)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario,
            'usuario':usuario,
            'vehiculo': vehiculo
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
    return render(request, 'TicketsHTMLS/formupdatetickets.html',dicformTIC)


def borrarticket(request, id):
    ticket = tickets.objects.get(id = id)
    ticket.delete()
    return redirect('inicio')


def graficoTickets(request):
    ticket = tickets.objects.values()
    valores = pd.DataFrame(ticket)
    print(valores)
    y = valores['destino']
    x = valores['horario']
    colors = np.random.randint(6 , size=(6))
    print(y,x)
    plt.title("horario y su destino")
    plt.suptitle("grafico de los tickets")
    plt.scatter(y,x, c=colors)
    plt.colorbar()
    plt.show()
    return redirect('inicio') 
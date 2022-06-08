from django.shortcuts import  redirect, render
from .models import tickets, Ciudades, Tarifas, Horario
from .forms import ticketsForm


# Create your views here.
def inicio(request):
     ticket = tickets.objects.raw('SELECT t.id, c.ciudad, cd.ciudadD, h.hora_salida, ta.precios FROM modulotickets_tickets as t, ciudades as c, ciudadesd as cd, horario as h, tarifas as ta where c.id = t.inicio  AND cd.id = t.destino AND h.id = t.horario AND ta.id = t.tarifa')
     dicTIC = {
          'tickets': ticket
     }
     return render(request, "TicketsHTMLS/tickets.html", dicTIC)


def formrtickets(request):
     ciudad = Ciudades.objects.all()
     tarifas = Tarifas.objects.all() 
     horario = Horario.objects.all() 
     if(request.method == 'GET'):
          forms = ticketsForm()
          dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario  
          }
     else:
         forms = ticketsForm(request.POST)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario  
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
     return render(request, 'TicketsHTMLS/formtickets.html',dicformTIC)


def editarticket(request , id):
    ciudad = Ciudades.objects.all()
    tarifas = Tarifas.objects.all()
    horario = Horario.objects.all() 
    ticket = tickets.objects.get(id = id)
    if(request.method == 'GET'):
       forms = ticketsForm(instance = ticket)
       dicformTIC ={
              'form': forms,
              'ciudad':ciudad,
              'tarifas':tarifas,
              'horario':horario
         } 
    else:
         forms = ticketsForm(request.POST, instance = ticket)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad,
            'tarifas':tarifas,
            'horario':horario
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
    return render(request, 'TicketsHTMLS/formupdatetickets.html',dicformTIC)


def borrarticket(request, id):
    ticket = tickets.objects.get(id = id)
    ticket.delete()
    return redirect('inicio')
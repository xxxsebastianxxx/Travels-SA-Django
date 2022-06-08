from django.shortcuts import  redirect, render
from .models import tickets, Ciudades
from .forms import ticketsForm


# Create your views here.
def inicio(request):
     ticket = tickets.objects.raw('SELECT t.id, c.ciudad, cd.ciudadD, t.horario, t.tarifa FROM modulotickets_tickets as t, ciudades as c, ciudadesd as cd where c.id = t.inicio  AND cd.id = t.destino')
     dicTIC = {
          'tickets': ticket
     }
     return render(request, "TicketsHTMLS/tickets.html", dicTIC)


def formrtickets(request):
     ciudad = Ciudades.objects.all()
     if(request.method == 'GET'):
          forms = ticketsForm()
          dicformTIC ={
            'form':forms,
            'ciudad':ciudad 
          }
     else:
         forms = ticketsForm(request.POST)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad 
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
     return render(request, 'TicketsHTMLS/formtickets.html',dicformTIC)


def editarticket(request , id):
    ciudad = Ciudades.objects.all()
    ticket = tickets.objects.get(id = id)
    if(request.method == 'GET'):
       forms = ticketsForm(instance = ticket)
       dicformTIC ={
              'form': forms,
              'ciudad':ciudad
         } 
    else:
         forms = ticketsForm(request.POST, instance = ticket)
         dicformTIC ={
            'form':forms,
            'ciudad':ciudad
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicio')
    return render(request, 'TicketsHTMLS/formupdatetickets.html',dicformTIC)


def borrarticket(request, id):
    ticket = tickets.objects.get(id = id)
    ticket.delete()
    return redirect('inicio')
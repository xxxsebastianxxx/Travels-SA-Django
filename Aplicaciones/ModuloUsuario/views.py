
from ast import Delete
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import usuarioForm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Create your views here.
def inicio(request):
    usuario = Usuario.objects.all()
    dicUSU ={
        'Usuarios':usuario
    }
    return render(request, "UsuariosHTMLS/usuario.html", dicUSU)

def formregistro(request):
    
     if(request.method == 'GET'):
          forms = usuarioForm()
          dicformUsu ={
            'form':forms
          }
     else:
         forms = usuarioForm(request.POST)
         dicformUsu ={
            'form':forms
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicioU')
     return render(request, 'UsuariosHTMLS/formregistro.html',dicformUsu)

def editarUsuario(request , id):
    usuario = Usuario.objects.get(id = id)
    if(request.method == 'GET'):
       forms = usuarioForm(instance = usuario)
       dicformUsu ={
              'form': forms
         } 
    else:
         forms = usuarioForm(request.POST, instance = usuario)
         dicformUsu ={
            'form':forms
          }
         if forms.is_valid():
              forms.save()
              return redirect('inicioU')
    return render(request, 'UsuariosHTMLS/formregistro.html',dicformUsu)

def borrarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('inicioU')



def graficoUsuarios(request):
     usuario = Usuario.objects.values()
     valores = pd.DataFrame(usuario)
     print(valores)
     y = valores['id']
     x = valores['nombre']
     print(y , x)
     plt.title("nombre y su id")
     plt.suptitle("grafico de los usuario")
     plt.bar(x , y)
     plt.show()
     return redirect('inicioU')     

from ast import Delete
from django.shortcuts import redirect, render
from .models import Usuario
from .forms import usuarioForm
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


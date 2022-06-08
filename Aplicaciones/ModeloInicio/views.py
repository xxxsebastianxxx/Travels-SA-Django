from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "InicioHTMLS/index.html",{})

def menu(request):
    return render(request, "InicioHTMLS/menu.html",{})


def mision(request):
    return render(request, "InicioHTMLS/mision.html",{})


def contacto(request):
    return render(request, "InicioHTMLS/contacto.html",{})
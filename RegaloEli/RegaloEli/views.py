from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from RegaloEli.forms import *
from RegaloEli.models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


# PAGINA DE INICIO DEL BLOG

def inicio(request):
    
    return render(request, "RegaloEli/inicio.html")

# Elegir telefono

def formulario_regalo(request):
    if request.method != "POST":
        return render(request, "RegaloEli/formulario_regalo.html")

    Pedido = Modelo(
        modelo=request.POST["modelo"],
        
    )
    if Pedido == "iPhone 14":
        return render(request, "RegaloEli/formulario_regalo2.html")
    else:
        Pedido.save()
    return render(request, "RegaloEli/inicio.htm")

def formulario_regalo2(request):
    if request.method != "POST":
        return render(request, "RegaloEli/formulario_regalo2.html")

    Capacidad = Memoria(
        memoria=request.POST["memoria"],
        
    )
    Capacidad.save()
    return render(request, "RegaloEli/inicio.htm")

def formulario_regalo3(request):
    if request.method != "POST":
        return render(request, "RegaloEli/formulario_regalo3.html")

    Pigmento = Color(
        
        color=request.POST["color"],
    )
    Pigmento.save()
    return render(request, "RegaloEli/inicio.htm")

def fin(request):
    
    return render(request, "RegaloEli/fin.html")

def intermedio(request):
    
    return render(request, "RegaloEli/intermedio.html")

def intermedio2(request):
    
    return render(request, "RegaloEli/intermedio2.html")



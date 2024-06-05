from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def carrito(request):
    return render(request, "carrito.html")

def inicio(request):
    return render(request, "inicio.html")

def login(request):
    return render(request, "login.html")

def despliegue(request):
    return render(request, "despliegue_producto.html")

def formulario(request):
    return render(request, "formulario_producto.html")
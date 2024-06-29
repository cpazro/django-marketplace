from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

@login_required
def todos(request):

    request.session ["usuario"] = "cpazro"
    usuario=request.session.get("usuario")
    context = {"usuario": usuario}

    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
    return render(request, "todos.html", context)

    
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

def login2(request):
    return render(request, "login2.html")
from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUserForm
# Create your views here.
def home(request):
    return render(request, "home.html")

from django.contrib.auth.forms import UserCreationForm

@login_required
def todos(request):

    request.session ["usuario"] = "cpazro"
    usuario=request.session.get("usuario")
    context = {"usuario": usuario}

    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
    return render(request, "todos.html", context)

def registro_user(request):
    if request.method == "POST":
        form = RegistroUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse("Usuario creado")
    else:
        form = RegistroUserForm()

    return render(request, 'registro_user.html', {'form': form})

def carrito(request):
    return render(request, "carrito.html")

def inicio(request):
    return render(request, "inicio.html")

def login(request, user):
    return render(request, "login.html")

def despliegue(request):
    return render(request, "despliegue_producto.html")

def formulario(request):
    return render(request, "formulario_producto.html")

def login2(request):
    return render(request, "login2.html")
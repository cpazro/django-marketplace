from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("todos/", views.todos, name="Todos"),
    path("carrito/", views.carrito, name="Carrito"),
    path("inicio/", views.inicio, name="Inicio"),
    path("despliegue-producto/", views.despliegue, name="despliegue-producto"),
    path("formulario-producto/", views.formulario, name="formulario-producto"),
    path("login/", views.login, name="login"),
]


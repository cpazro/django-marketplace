from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.inicio, name="home"),
    path("admin/", admin.site.urls),
    path("todos/", views.todos, name="Todos"),
    path("carrito/", views.carrito, name="carrito"),
    path("carrito/inicio/", views.inicio, name="inicio"),
    path("carrito/despliegue-producto/", views.despliegue, name="despliegue-producto"),
    path("carrito/formulario-producto/", views.formulario, name="formulario-producto"),
    path('carrito/login', views.login, name='login'),
]


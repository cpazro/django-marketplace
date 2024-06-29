from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path("", views.inicio, name="home"),
    path("admin/", admin.site.urls),
    path("carrito/todos/", views.todos, name="todos"),
    path("carrito/", views.carrito, name="carrito"),
    path("carrito/inicio/", views.inicio, name="inicio"),
    path("carrito/despliegue-producto/", views.despliegue, name="despliegue-producto"),
    path("carrito/formulario-producto/", views.formulario, name="formulario-producto"),
    path('carrito/login', views.login, name='login'),
    
]


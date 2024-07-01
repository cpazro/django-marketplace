from django.contrib import admin
from .models import TodoItem, Cliente, TipoTarjeta, Tarjeta

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'fecha_nacimiento', 'correo', 'es_miembro')
    search_fields = ('nombre', 'correo')

class TipoTarjetaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo', 'descripcion')
    search_fields = ('descripcion',)
    list_filter = ('descripcion',)  # Optional: Add filters for descriptions if there are many types

class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('numero_tarjeta', 'nombre', 'tipo', 'cliente')
    search_fields = ('numero_tarjeta', 'nombre')
    list_filter = ('tipo',)

admin.site.register(TodoItem)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(TipoTarjeta, TipoTarjetaAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
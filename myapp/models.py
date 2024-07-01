from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    clave = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    es_miembro = models.BooleanField(default=False)  # Boolean field

    def __str__(self):
        return self.nombre

class TipoTarjeta(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Tarjeta(models.Model):
    numero_tarjeta = models.IntegerField()
    cvv = models.IntegerField()
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoTarjeta, on_delete=models.CASCADE)  # Foreign Key to TipoTarjeta
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Foreign Key to Cliente

    def __str__(self):
        return f"{self.numero_tarjeta} - {self.nombre}"
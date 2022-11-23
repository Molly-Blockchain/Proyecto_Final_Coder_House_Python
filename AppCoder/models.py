# ___________ Zona de imports ___________

from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from distutils.command.upload import upload



# ___________ Lista de modelos ___________

class Libro(models.Model):
    nombreLibro = models.CharField(max_length = 100)
    anioPublicacion = models.IntegerField()
    genero = models.CharField(max_length = 100)
    fechaIngreso = models.DateField()
    precio = models.IntegerField()

    def __str__(self):
        return f"Nombre Libro: {self.nombreLibro} - Anio de publicacion: {self.anioPublicacion} - Genero: {self.genero} - Fecha de ingreso: {self.fechaIngreso} - Precio: {self.precio}"


class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono}"


class Bibliotecario(models.Model):
    nombreBibliotecario = models.CharField(max_length = 50)
    apellidoBibliotecario = models.CharField(max_length = 40)
    
    def __str__(self):
        return f"Nombre bibliotecario: {self.nombreBibliotecario} - Apellido bibliotecario: {self.apellidoBibliotecario}"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)
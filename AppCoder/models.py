
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
from distutils.command.upload import upload


# _______________ Lista de modelos _______________

# ___________ Libro ___________

class Libro(models.Model):
    nombreLibro = models.CharField(max_length = 40)
    anioPublicacion = models.IntegerField()
    genero = models.CharField(max_length = 40)
    fechaIngreso = models.DateField()
    precio = models.IntegerField()
    def __str__(self):
        return f"Nombre libro: {self.nombreLibro} - Anio de publicacion: {self.anioPublicacion} - Genero: {self.genero} - Fecha de ingreso: {self.fechaIngreso} - Precio: {self.precio}"


# ___________ Cliente ___________

class Cliente(models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    telefono = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: {self.telefono}"


# ___________ Bibliotecario ___________

class Bibliotecario(models.Model):
    nombreBibliotecario = models.CharField(max_length = 40)
    apellidoBibliotecario = models.CharField(max_length = 40)
    def __str__(self):
        return f"Nombre bibliotecario: {self.nombreBibliotecario} - Apellido bibliotecario: {self.apellidoBibliotecario}"


# ___________ Avatar ___________

# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)
# ___________ Zona de imports ___________

from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# ___________ Formularios ___________

class LibroFormulario(forms.Form):
    nombreLibro = forms.CharField(max_length = 100)
    anioPublicacion = forms.IntegerField()
    genero = forms.CharField(max_length = 100)
    fechaIngreso = forms.DateField()
    precio = forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length = 100)
    apellido = forms.CharField(max_length = 100)
    telefono = forms.IntegerField()

class BibliotecarioFormulario(forms.Form):
    nombreBibliotecario = forms.CharField(max_length = 50)
    apellidoBibliotecario = forms.CharField(max_length = 40)
    


# ___________ Usuarios ___________

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contrasenia', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la contrasenia', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label = "Modificar E-mail")
    password1= forms.CharField(label = 'Contrasenia Antigua', widget = forms.PasswordInput)
    password2= forms.CharField(label = 'Repetir la contrasenia Antigua', widget = forms.PasswordInput)

    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}        
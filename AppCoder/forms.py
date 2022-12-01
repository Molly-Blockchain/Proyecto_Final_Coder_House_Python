from dataclasses import field
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# _______________ Lista de formularios _______________

# ___________ Formulario Libro ___________

class LibroFormulario(forms.Form):
    nombreLibro = forms.CharField(max_length = 40)
    anioPublicacion = forms.IntegerField()
    genero = forms.CharField(max_length = 40)
    fechaIngreso = forms.DateField()
    precio = forms.IntegerField()


# ___________ Formulario Cliente ___________

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length = 40)
    telefono = forms.IntegerField()


# ___________ Formulario Bibliotecario ___________

class BibliotecarioFormulario(forms.Form):
    nombreBibliotecario = forms.CharField(max_length = 40)
    apellidoBibliotecario = forms.CharField(max_length = 40)
    

# ___________ Formulario de registro de usuarios ___________

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la contraseña', widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k : "" for k in fields}


# ___________ Formulario de edición de usuarios ___________

class UserEditForm(UserCreationForm):
   
    email = forms.EmailField(label = "Modificar E-mail")
    password1 = forms.CharField(label = 'Contraseña Antigua', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir la contraseña Antigua', widget = forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k : "" for k in fields}        
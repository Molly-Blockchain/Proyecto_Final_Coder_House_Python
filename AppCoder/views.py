# ___________ Zona de imports ___________

from django.shortcuts import render
from django.http import HttpResponse


# ___________ Importamos modelos y formularios ___________

from AppCoder.forms import LibroFormulario, ClienteFormulario, UserRegisterForm, BibliotecarioFormulario, UserEditForm
from AppCoder.models import Libro, Cliente, Bibliotecario, Avatar


# ___________ CBV ___________

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ___________ Inicio de sesión ___________

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

 

# ___________ Creación de vistas ___________

# ___________ Libro ___________

def libro(request):
    return render(request, "AppCoder/libro.html")

@login_required

def leerLibro(request):
    libros = Libro.objects.all()
    contexto = {"libros" : libros}
    return render(request, "AppCoder/libro.html", contexto)

def formularioLibro(request):
    if request.method == 'POST':
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            libro = Libro(
                nombreLibro = informacion['nombreLibro'],
                anioPublicacion = informacion['anioPublicacion'],
                genero = informacion['genero'],
                fechaIngreso = informacion['fechaIngreso'],
                precio = informacion['precio'])
		    
            libro.save()

            libros = Libro.objects.all()
    
            return render(request,"AppCoder/libro.html", {"libros" : libros})

    else:
        miFormulario = LibroFormulario()
    return render(request, "AppCoder/formularioLibro.html", {"miFormulario" : miFormulario})



def editarLibro(request, libro_nombre):

    libro = Libro.objects.get(nombreLibro = libro_nombre)

    if request.method == 'POST':
        miFormularioLibro = LibroFormulario(request.POST)
        print(miFormularioLibro)

        if miFormularioLibro.is_valid:
            
            informacion = miFormularioLibro.cleaned_data
		    
            libro.nombreLibro = informacion['nombre libro']
            libro.anioPublicacion = informacion['anio de publicacion']
            libro.genero = informacion['genero']
            libro.fechaIngreso = informacion['fecha de ingreso']
            libro.precio = informacion['precio']
		    
            libro.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioLibro = LibroFormulario(
            initial = {'nombreLibro' : libro.nombreLibro,
                'anio de publicacion': libro.anioPublicacion, 
                'genero' : libro.genero,
                'fecha de ingreso' : libro.fechaIngreso,
                'precio' : libro.precio})
    
    return render(request, "AppCoder/editarLibro.html", {"miFormularioLibro": miFormularioLibro, "libro_nombre" : libro_nombre})
        


def eliminarLibro(request, libro_nombre):
    libro = Libro.objects.get(nombreLibro = libro_nombre)
    libro.delete()
    libros = Libro.objects.all()
    contexto = {"libros" : libros}
    return render(request,"AppCoder/libro.html", contexto)


@login_required

def busquedaLibro(request):
    return render(request, "AppCoder/busquedaLibro.html")
    

@login_required

def buscar(request):
        
    if request.GET["nombreLibro"]:
        nombreLibro = request.GET['nombreLibro']
        libros = Libro.objects.filter(nombreLibro__icontains = nombreLibro)
        
        return render(request, "AppCoder/libro.html", {"libros" : libros})

    else:
        respuesta = "No enviaste nada"
    return render(request, "AppCoder/inicio.html", {"respuesta" : respuesta})



# ___________ Cliente ___________

def cliente(request):
    return render(request, "AppCoder/cliente.html")


@login_required

def leerCliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes" : clientes}
    return render(request, "AppCoder/cliente.html", contexto)


def formularioCliente(request):

    if request.method == 'POST':
        miFormularioCliente = ClienteFormulario(request.POST)
        print(miFormularioCliente)

        if miFormularioCliente.is_valid:
            
            informacion = miFormularioCliente.cleaned_data
		    
            cliente = Cliente(
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                telefono = informacion['telefono'])
		    
            cliente.save()

            clientes = Cliente.objects.all()
            
            return render(request,"AppCoder/cliente.html", {"clientes" : clientes})

    else:
        miFormularioCliente = ClienteFormulario()
    return render(request, "AppCoder/formularioCliente.html", {"miFormularioCliente" : miFormularioCliente})



def editarCliente(request, cliente_nombre):

    cliente = Cliente.objects.get(nombre = cliente_nombre)

    if request.method == 'POST':
        miFormularioCliente = ClienteFormulario(request.POST)
        print(miFormularioCliente)

        if miFormularioCliente.is_valid:
            
            informacion = miFormularioCliente.cleaned_data
		    
            cliente.nombre = informacion['nombre']
            cliente.apellido = informacion['apellido']
            cliente.telefono = informacion['telefono']
		    
            cliente.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioCliente = ClienteFormulario(
            initial = {'nombre': cliente.nombre,
            'apellido' : cliente.apellido,
            'telefono' : cliente.telefono}) 
    
    return render(request, "AppCoder/editarCliente.html", {"miFormularioCliente" : miFormularioCliente, "cliente_nombre" : cliente_nombre})
        

def eliminarCliente(request, cliente_nombre):
    cliente = Cliente.objects.get(nombre = cliente_nombre)
    cliente.delete()
    clientes = Cliente.objects.all()
    contexto = {"clientes" : clientes}
    return render(request,"AppCoder/cliente.html", contexto)



# ___________ Cliente (CBV, herencia) ___________

class ClienteList(ListView):
    model = Cliente
    template_name = "AppCoder/cliente_list.html"


class ClienteDetalle(DetailView): 
    model = Cliente
    template_name = "AppCoder/cliente_detalle.html"

class ClienteCreacion(CreateView):
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"	
    fields = ['nombre','apellido','telefono']


class ClienteUpdate(UpdateView):    
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"	
    fields = ['nombre','apellido','telefono']


class ClienteDelete(DeleteView):
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"



# ___________ Bibliotecario ___________

def bibliotecario(request):
    return render(request,"AppCoder/bibliotecario.html")


@login_required

def leerBibliotecario(request):
    bibliotecarios = Bibliotecario.objects.all()
    contexto = {"bibliotecarios" : bibliotecarios}
    return render(request,"AppCoder/bibliotecario.html", contexto)

def formularioBibliotecario(request):

    if request.method == 'POST':
        miFormularioBibliotecario = BibliotecarioFormulario(request.POST)
        print(miFormularioBibliotecario)

        if miFormularioBibliotecario.is_valid:
            
            informacion = miFormularioBibliotecario.cleaned_data
		    
            bibliotecario = Bibliotecario(
                nombreBibliotecario = informacion['nombreBibliotecario'],
                apellidoBibliotecario = informacion['apellidoBibliotecario'])
		    
            bibliotecario.save()

            bibliotecarios = Bibliotecario.objects.all()
            
            contexto = {"bibliotecarios" : bibliotecarios}
            return render(request,"AppCoder/bibliotecario.html", contexto)

    else:
        miFormularioBibliotecario = BibliotecarioFormulario()
    return render(request, "AppCoder/formularioBibliotecario.html", {"miFormularioBibliotecario" : miFormularioBibliotecario})



# ___________ Login & Registro de usuarios ___________

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje" : f"Bienvenido {usuario}"})
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje" : "Error, datos incorrectos"})

        else:
            
                return render(request, "AppCoder/inicio.html", {"mensaje" : "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form' : form})


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje" : "Usuario creado con éxito"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request, "AppCoder/registro.html", {"form" : form})


def inicio(request):
    return render(request, "AppCoder/inicio.html")


@login_required

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']            
            usuario.save()
            

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email' : usuario.email})
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario" : miFormulario, "usuario" : usuario})



'''

# ___________ Avatar ___________

@login_required

def inicio(request):
    avatares = Avatar.objects.filter(user = request.user.id)

    return render(request, "AppCoder/inicio.html", {"url" : avatares[0].imagen.url})

'''
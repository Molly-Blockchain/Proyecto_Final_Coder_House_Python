from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import LibroFormulario, ClienteFormulario, UserRegisterForm, BibliotecarioFormulario, UserEditForm
from AppCoder.models import Libro, Cliente, Bibliotecario #, Avatar

# _____ CVB _____
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# _____ Loguin _____
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

 

# _______________ Lista de vistas (funciones) _______________

# ___________ Vista Libro ___________

def libro(request):
    return render(request, "AppCoder/libro.html")


@login_required


def leerDocumento(request):
    documentos = Libro.objects.all()
    contexto = {"documentos" : documentos}
    return render(request, "AppCoder/libro.html", contexto)


# _____ Formulario Libro _____

def formularioDocumento(request):
    if request.method == 'POST':
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            documento = Libro(
                
                nombreLibro = informacion['nombreLibro'],
                anioPublicacion = informacion['anioPublicacion'],
                genero = informacion['genero'],
                fechaIngreso = informacion['fechaIngreso'],
                precio = informacion['precio']
                
                )
		    
            documento.save()

            documentos = Libro.objects.all()
    
            return render(request, "AppCoder/libro.html", {"documentos" : documentos})

    else:
        miFormulario = LibroFormulario()
    return render(request, "AppCoder/formularioDocumento.html", {"miFormulario" : miFormulario})


# _____ Formulario Editar Libro _____

def editarDocumento(request, documento_nombre):

    documento = Libro.objects.get(nombreLibro = documento_nombre)

    if request.method == 'POST':
        miFormularioDocumento = LibroFormulario(request.POST)
        print(miFormularioDocumento)

        if miFormularioDocumento.is_valid:
            
            informacion = miFormularioDocumento.cleaned_data
		    
            documento.nombreLibro = informacion['nombreLibro']
            documento.anioPublicacion = informacion['anioPublicacion']
            documento.genero = informacion['genero']
            documento.fechaIngreso = informacion['fechaIngreso']
            documento.precio = informacion['precio']
		    
            documento.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioDocumento = LibroFormulario(
            initial =  {'nombreLibro' : documento.nombreLibro,
                        'anioPublicacion' : documento.anioPublicacion,
                        'genero' : documento.genero,
                        'fechaIngreso' : documento.fechaIngreso,
                        'precio': documento.precio}
            ) 
    
    return render(request, "AppCoder/editarDocumento.html", {"miFormularioDocumento" : miFormularioDocumento, "documento_nombre" : documento_nombre})


# _____ Eliminar Libro _____

def eliminarDocumento(request, documento_nombre):
    documento = Libro.objects.get(nombreLibro = documento_nombre)
    documento.delete()
    documentos = Libro.objects.all()
    contexto = {"documentos" : documentos}
    return render(request, "AppCoder/libro.html", contexto)


@login_required


# _____ Buscar Libro _____

def busquedaDocumento(request):
    return render(request, "AppCoder/busquedaDocumento.html")

    
@login_required


def buscar(request):
        
    if request.GET["nombreLibro"]:
        nombreLibro = request.GET['nombreLibro']
        documentos = Libro.objects.filter(nombreLibro__icontains = nombreLibro)
        
        return render(request, "AppCoder/libro.html", {"documentos" : documentos})

    else:
        respuesta = "No enviaste nada"
    return render(request, "AppCoder/inicio.html", {"respuesta" : respuesta})


# ___________ Vista Cliente ___________

# _____ Vista Cliente _____

def cliente(request):
    return render(request, "AppCoder/cliente.html")


@login_required


def leerCliente(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes" : clientes}
    return render(request, "AppCoder/cliente.html", contexto)


# _____ Formulario Cliente _____

def formularioCliente(request):

    if request.method == 'POST':
        miFormularioCliente = ClienteFormulario(request.POST)
        print(miFormularioCliente)

        if miFormularioCliente.is_valid:
            
            informacion = miFormularioCliente.cleaned_data
		    
            cliente = Cliente(
                
                nombre = informacion['nombre'],
                apellido = informacion['apellido'],
                telefono = informacion['telefono']
                )
		    
            cliente.save()

            clientes = Cliente.objects.all()
            
            return render(request, "AppCoder/cliente.html", {"clientes" : clientes})

    else:
        miFormularioCliente = ClienteFormulario()
    return render(request, "AppCoder/formularioCliente.html", {"miFormularioCliente" : miFormularioCliente})


# _____ Formulario Editar Cliente _____

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
        miFormularioCliente = ClienteFormulario(initial = {
            'nombre' : cliente.nombre,
            'apellido' : cliente.apellido,
            'telefono' : cliente.telefono
            }) 
    
    return render(request, "AppCoder/editarCliente.html", {
        "miFormularioCliente" : miFormularioCliente,
        "cliente_nombre" : cliente_nombre
        })


# _____ Eliminar Cliente _____

def eliminarCliente(request, cliente_nombre):
    cliente = Cliente.objects.get(nombre = cliente_nombre)
    cliente.delete()
    clientes = Cliente.objects.all()
    contexto = {"clientes" : clientes}
    return render(request, "AppCoder/cliente.html", contexto)


# ___________ Cliente CBV ___________

class ClienteList(ListView):
    model = Cliente
    template_name = "AppCoder/cliente_list.html"


class ClienteDetalle(DetailView): 
    model = Cliente
    template_name = "AppCoder/cliente_detalle.html"

class ClienteCreacion(CreateView):
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"	
    fields = ['nombre', 'apellido', 'telefono']


class ClienteUpdate(UpdateView):
    
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"	
    fields = ['nombre', 'apellido', 'telefono']


class CursoDelete(DeleteView):  
    model = Cliente
    succcess_url = "/AppCoder/cliente/list"	


# ___________ Vista Bibliotecario ___________

# _____ Vista Bibliotecario _____

def bibliotecario(request):
    return render(request, "AppCoder/bibliotecario.html")


@login_required


def leerBibliotecario(request):
    bibliotecarios = Bibliotecario.objects.all()
    contexto = {"bibliotecarios" : bibliotecarios}
    return render(request, "AppCoder/bibliotecario.html", contexto)


# _____ Formulario Bibliotecario _____

def formularioBibliotecario(request):

    if request.method == 'POST':
        miFormularioBibliotecario = BibliotecarioFormulario(request.POST)
        print(miFormularioBibliotecario)

        if miFormularioBibliotecario.is_valid:
            
            informacion = miFormularioBibliotecario.cleaned_data
		    
            bibliotecario = Bibliotecario(
                
                nombreBibliotecario = informacion['nombreBibliotecario'],
                apellidoBibliotecario = informacion['apellidoBibliotecario']
                )
		    
            bibliotecario.save()

            bibliotecarios = Bibliotecario.objects.all()
            
            contexto = {"bibliotecarios" : bibliotecarios}
            return render(request, "AppCoder/bibliotecario.html", contexto)

    else:
        miFormularioBibliotecario = BibliotecarioFormulario()
    return render(request, "AppCoder/formularioBibliotecario.html", {"miFormularioBibliotecario" : miFormularioBibliotecario})


# _____ Formulario Editar Bibliotecario _____

def editarBibliotecario(request, bibliotecario_nombre):

    bibliotecario = Bibliotecario.objects.get(nombreBibliotecario = bibliotecario_nombre)

    if request.method == 'POST':
        miFormularioBibliotecario = BibliotecarioFormulario(request.POST)
        print(miFormularioBibliotecario)

        if miFormularioBibliotecario.is_valid:
            
            informacion = miFormularioBibliotecario.cleaned_data
		    
            bibliotecario.nombreBibliotecario = informacion['nombreBibliotecario']
            bibliotecario.apellidoBibliotecario = informacion['apellidoBibliotecario']
            
            bibliotecario.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioBibliotecario = BibliotecarioFormulario(initial = {
            'nombreBibliotecario' : bibliotecario.nombreBibliotecario,
            'apellidoBibliotecario' : bibliotecario.apellidoBibliotecario
            }) 
    
    return render(request, "AppCoder/editarBibliotecario.html", {
        "miFormularioBibliotecario" : miFormularioBibliotecario,
        "bibliotecario_nombre" : bibliotecario_nombre
        })


# _____ Eliminar Bibliotecario _____

def eliminarBibliotecario(request, bibliotecario_nombre):
    bibliotecario = Bibliotecario.objects.get(nombreBibliotecario = bibliotecario_nombre)
    bibliotecario.delete()
    bibliotecarios = Bibliotecario.objects.all()
    contexto = {"bilbiotecarios" : bibliotecarios}
    return render(request, "AppCoder/bibliotecario.html", contexto)


# ___________ Loguin/Register ___________

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

        miFormulario = UserEditForm(initial = {'email' : usuario.email})
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario" : miFormulario, "usuario" : usuario})


# ___________ Vista Avatar ___________

# @login_required
# def inicio(request):
#     avatares = Avatar.objects.filter(user=request.user.id)

#     return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})

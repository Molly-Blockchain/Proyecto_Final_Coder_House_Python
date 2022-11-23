# ___________ Zona de imports ___________

from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView



# ___________ URLs ___________

urlpatterns = [
    path('', views.inicio, name = 'inicio'),


    # ___________ Libro ___________

    path('libro.html', views.libro, name = 'libro'),
    path('libro.html', views.leerLibro, name = 'leerLibro'),
    path('formularioLibro', views.formularioLibro, name = 'formularioLibro'),
    path('eliminarLibro/<libro_nombre>/', views.eliminarLibro, name = 'eliminarLibro'),
    path('editarLibro/<libro_nombre>/', views.editarLibro, name = 'editarLibro'),
    path('busquedaLibro', views.busquedaLibro, name = 'busquedaLibro'),
    path('buscar/', views.buscar),


    # ___________ Cliente ___________

    path('cliente', views.cliente, name = 'cliente'),
    path('formularioCliente', views.formularioCliente, name = 'formularioCliente'),
    path('leerCliente', views.leerCliente, name = 'leerCliente'), 
    path('eliminarCliente/<cliente_nombre>/',views.eliminarCliente, name = 'eliminarCliente'),
    path('editarCliente/<cliente_nombre>/', views.editarCliente, name = 'editarCliente'),


    # ___________ Bibliotecario ___________

    path('bibliotecario', views.bibliotecario, name = 'bibliotecario'),
    path('formularioBibliotecario', views.formularioBibliotecario, name = 'formularioBibliotecario'),
    path('leerBibliotecario', views.leerBibliotecario, name = 'leerBibliotecario'), 
    
    #   path('eliminarBibliotecario/<bibliotecario_nombre>/', views.eliminarBibliotecario, name = 'eliminarBibliotecario'),
    #   path('editarBibliotecario/<bibliotecario_nombre>/', views.editarBibliotecario, name = 'editarBibliotecario'),


    # ___________ Inicio de sesión & Registro de usuarios ___________
    
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name = 'AppCoder/logout.html'), name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name = "EditarPerfil"),
    
]
from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    
    # ___________ Libro ___________
    path('documento', views.libro, name = 'documento'),
    path('formularioDocumento', views.formularioDocumento, name = 'formularioDocumento'),
    path('leerDocumento', views.leerDocumento, name = 'leerDocumento'),
    path('eliminarDocumento/<documento_nombre>/', views.eliminarDocumento, name = 'eliminarDocumento'),
    path('editarDocumento/<documento_nombre>/', views.editarDocumento, name = 'editarDocumento'),
    path('busquedaDocumento', views.busquedaDocumento, name = 'busquedaDocumento'),
    path('buscar/', views.buscar),
    
    # ___________ Cliente ___________
    path('cliente', views.cliente, name = 'cliente'),
    path('formularioCliente', views.formularioCliente, name = 'formularioCliente'),
    path('leerCliente', views.leerCliente, name = 'leerCliente'), 
    path('eliminarCliente/<cliente_nombre>/', views.eliminarCliente, name = 'eliminarCliente'),
    path('editarCliente/<cliente_nombre>/', views.editarCliente, name = 'editarCliente'),

    # ___________ Bibliotecario ___________
    path('bibliotecario', views.bibliotecario, name = 'bibliotecario'),
    path('formularioBibliotecario', views.formularioBibliotecario, name = 'formularioBibliotecario'),
    path('leerBibliotecario', views.leerBibliotecario, name = 'leerBibliotecario'), 
    path('eliminarBibliotecario/<bibliotecario_nombre>/', views.eliminarBibliotecario, name = 'eliminarBibliotecario'),
    path('editarBibliotecario/<bibliotecario_nombre>/', views.editarBibliotecario, name = 'editarBibliotecario'),

    # ___________ Loguin/Register ___________
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name = 'AppCoder/logout.html'), name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name = "EditarPerfil"),
    
]
# Proyecto Final Python Coder House 2022 


# Comision 44065, realizado por: Lucas López y Matias Milio

Este proyecto fue desarrollado en Python utilizando el framework Django. 
El proyecto trata aplicación web sobre una bilbioteca, donde se pueden observar los diferentes registros de la base de datos, agregar items, editarlos e incluso eliminarlos

Debajo se encuentra el link para ver la app en funcionamiento 


# Video Demostración

https://youtu.be/u1sYk1Zi5jY

____________________________________________________________________________________________________________________________________________________________________


# Documentación del proyecto

Los archivos del proyecto son:
    - models.py
    - forms.py
    - urls.py
    - views.py
    - La carpeta de templates, entre otros.

____________________________________________________________________________________________________________________________________________________________________


# Models.py:

En este archivo podemos encontrar los modelos de datos utilizados en la app.

Modelo Libro: 
    Parámetros: 
        - nombreLibro (CharField, nombre del libro)
        - anioPublicacion (IntegerField, año de publicación del libro)
        - genero (CharField, genero del libro)
        - fechaIngreso (DateField, es la fecha de ingreso del libro a la biblioteca)
        - precio (IntegerField, el precio del libro en el mercado)

Modelo Cliente: 
    Parámetros:
    - nombre (CharField, nombre cliente de la biblioteca)
    - apellido (CharField, apellido del cliente de la biblioteca)
    - telefono (IntegerField, numero del cliente de la biblioteca)

Modelo Bibliotecario: 
    Parámetros:
    - nombreBibliotecario (CharField, nombre del bibliotecario)
    - apellidoBibliotecario (CharField, apellido del bibliotecario)

____________________________________________________________________________________________________________________________________________________________________


# Forms.py:

En este archivo podemos encontrar los formularios usados para cargar los datos que quedan guardados en nuestra base de datos.

____________________________________________________________________________________________________________________________________________________________________


# Urls.py:

Contiene cada una de las rutas de las vistas de la app. 

____________________________________________________________________________________________________________________________________________________________________


# Views.py:

Aparecen todas las vistas que se utilizan en la app.
Asociado a lo anterior por cada modelo se aplica el concepto de CRUD(Create, Read, Update, Delete); una vista de logueo, registro y edicion de perfil del usuario. Además tenemos la vista para buscar una mascota por su nombre.


Ejemplo de CRUD para el Modelo Libro (views.py):

Create: vista formularioDocumento

Read: vista leerDocumento

Update: vista editarDocumento

Delete: vista eliminarDocumento

____________________________________________________________________________________________________________________________________________________________________


# Templates:
Es una carpeta donde se encuentran todos los archivos .HTML usados por la app.
Se utilza una platilla de BOOSTRAP y se aplica el concepto de herencia a cada archivo.

____________________________________________________________________________________________________________________________________________________________________
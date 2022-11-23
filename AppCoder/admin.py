# ___________ Zona de imports ___________

from django.contrib import admin
from .models import *



# ___________ Registro de modelos ___________

admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Bibliotecario)
admin.site.register(Avatar)

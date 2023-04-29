from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('', home, name="inicio"),
    path('libros/', lista_libros, name="libros"),
    path('libros/nuevo', crear_libros, name="nuevo_libro"),
    path('libros/eliminar/<int:id>',
         eliminar_libro, name='eliminar_libro'),
    path('libros/buscar', buscar_libro, name="busqueda"),
]

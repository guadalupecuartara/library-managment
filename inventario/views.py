from django.shortcuts import render, redirect
from .models import *
from biblioteca.agregador import agregador


# Create your views here.


def home(request):
    return render(request, 'busqueda.html')


def lista_libros(request):
    libros = Libros.objects.all()
    return render(request, 'inventario.html', {'libros': libros})


def crear_libros(request):
    libro_data = agregador(request.POST['isbn'])
    libro = Libros(isbn=request.POST['isbn'],
                   titulo=libro_data['titulo'],
                   autor=libro_data['autor'],
                   genero=libro_data['genero'],
                   sinopsis=libro_data['sinopsis'],)
    libro.save()
    return redirect('/libros')


def eliminar_libro(request, id):
    libro = Libros.objects.get(id=id)
    libro.delete()
    return redirect('/libros/')


def buscar_libro(request):
    if request.method == 'POST':
        campo = request.POST['campo']
        if not request.POST['busqueda'] or campo == "Seleccione una opcion":
            return render(request, 'busqueda.html')
        libros = Libros.objects.filter(
            **{f'{campo}__icontains': request.POST['busqueda']})
        return render(request, 'inventario.html', {'libros': libros})
    else:
        return redirect('inicio')

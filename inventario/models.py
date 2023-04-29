from django.db import models

# Create your models here.


class Libros(models.Model):
    isbn = models.CharField(max_length=100, default="")
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    sinopsis = models.TextField()

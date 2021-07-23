from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    img = models.ImageField(upload_to = "categorias", blank = True, null = True)

    def __str__(self):
        return self.categoria

class Subcategoria(models.Model):
    subcategoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    img = models.ImageField(upload_to = "subcategorias", blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    def __str__(self):
        return self.subcategoria

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    img = models.ImageField(upload_to = "productos", blank = True, null = True)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE, blank = True, null = True)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=CASCADE, blank = True, null = True)
    # created_date = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)



from django.db import models

class Actividades(models.Model):
    contenido = models.TextField()
    precio = models.IntegerField()
    id_categoria = models.ForeignKey('Categorias',on_delete=models.CASCADE)
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    
class Valoraciones(models.Model):
    valoracion = models.PositiveSmallIntegerField(blank=True, null=True)
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    
class Comentarios(models.Model):
    comentario = models.TextField(null=True , blank=True)
    id_usuario = models.ForeignKey('Usuarios',on_delete=models.CASCADE)
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    
class ActividadesUsuarios(models.Model):
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('Usuarios',on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=100, unique=True)
    

from django.db import models
from django.contrib.auth.models import User

class Actividades(models.Model):
    nombre_actividad = models.TextField()
    descripcion_actividad = models.TextField(null=True , blank=True)
    imagen_actividad = models.TextField(null=True , blank=True)
    precio_actividad = models.IntegerField()

class Categorias(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

class Valoraciones(models.Model):
    valoracion = models.PositiveSmallIntegerField(blank=True, null=True)
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)

class Comentarios(models.Model):
    comentario = models.TextField(null=True , blank=True)
    usuario_comentario= models.TextField(null=True , blank=True)
    id_comentario = models.TextField(null=True , blank=True)

class ActividadesUsuarios(models.Model):
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('Usuarios',on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=100, unique=True)

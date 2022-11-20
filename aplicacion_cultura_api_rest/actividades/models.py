
from django.db import models

class Actividades(models.Model):
    contenido = models.TextField()
    precio = models.IntegerField()
    id_categoria = models.ForeignKey('Categorias',on_delete=models.CASCADE)
    img = models.TextField(null=True)
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=100,unique=True,primary_key=True)
    
class Valoraciones(models.Model):
    valoracion = models.PositiveSmallIntegerField(blank=True, null=True)
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    
class Comentarios(models.Model):
    comentario = models.TextField(null=True , blank=True)
    id_usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    
class ActividadesUsuarios(models.Model):
    id_actividad = models.ForeignKey('Actividades',on_delete=models.CASCADE)
    id_usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    


from rest_framework import serializers
from .models import Actividades, Comentarios


class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ("id", "nombre_actividad","descripcion_actividad", "imagen_actividad","precio_actividad")

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ("id", "comentario","id_comentario","usuario_comentario")
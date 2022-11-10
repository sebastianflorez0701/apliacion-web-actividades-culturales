from rest_framework import serializers
from .models import Actividades


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ("id", "nombre_actividad","descripcion_actividad", "imagen_actividad","precio_actividad")

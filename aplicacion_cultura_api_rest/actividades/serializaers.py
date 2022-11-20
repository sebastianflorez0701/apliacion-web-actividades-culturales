from rest_framework import serializers
from actividades.models import Actividades,Categorias,Comentarios,ActividadesUsuarios,Valoraciones
from django.contrib.auth.models import User

class SerializersActividades(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = ['contenido', 'precio', 'id_categoria','img']

class SerializersCategorias(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['nombre']

class SerializersValoraciones(serializers.ModelSerializer):
    class Meta:
        model = Valoraciones
        fields = ['id', 'valoracion', 'id_actividad']

class SerializersComentarios(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ['id', 'comentario', 'id_usuario', 'id_actividad']

class SerializersUsuarios(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'email','login']

class SerializersActividadesUsuarios(serializers.ModelSerializer):
    
    class Meta:
        model = ActividadesUsuarios
        fields = ['id_actividad', 'id_usuario']

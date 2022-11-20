from django.contrib import admin
from .models import Actividades,Categorias,Valoraciones,Comentarios, ActividadesUsuarios

admin.site.register(Actividades)
admin.site.register(Categorias)
admin.site.register(Valoraciones)
admin.site.register(Comentarios)
admin.site.register(ActividadesUsuarios)

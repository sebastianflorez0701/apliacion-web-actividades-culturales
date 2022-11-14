from .models import Actividades, Comentarios
from rest_framework import viewsets, permissions
from .serializers import ActividadesSerializer, ComentariosSerializer


class ProjectViewSetActividades(viewsets.ModelViewSet):
    queryset = Actividades.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ActividadesSerializer

class ProjectViewSetComentarios(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ComentariosSerializer
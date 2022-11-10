from .models import Actividades
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Actividades.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

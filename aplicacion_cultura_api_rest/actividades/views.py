
from actividades.models import Actividades
from actividades.serializaers import SerializersActividades
from rest_framework.views import APIView
from rest_framework.response import Response

class ActividadesList(APIView):
    def get(self, request, format = None):
        actividades = Actividades.objects.all().order_by('precio')[:3]
        serializer = SerializersActividades(actividades, many=True)
        return Response(serializer.data)
    
    
        



# Create your views here.

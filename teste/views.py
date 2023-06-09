from rest_framework import viewsets
from .serializers import ModeloSerializer
from .models import Modelo


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

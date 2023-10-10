from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet (viewsets.ModelViewSet):
    queryset = Project.objects.all() #Consultar todos los datos de una tabla
    permission_classes = [permissions.AllowAny] #lista de permisos, allowAny->cualquiera puede consultar
    serializer_class= ProjectSerializer #serializer previamente creado
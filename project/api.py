from .models import  project

from rest_framework import viewsets,permissions
from .serializer import ProjectSerialiser

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=project.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ProjectSerialiser






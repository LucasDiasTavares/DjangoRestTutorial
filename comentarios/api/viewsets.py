from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    """
    Pego todos os endereços
    """
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

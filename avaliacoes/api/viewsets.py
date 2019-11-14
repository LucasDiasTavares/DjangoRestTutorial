from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    """
    Pego todos os endereços
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

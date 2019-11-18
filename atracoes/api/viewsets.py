from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    """
    Pego todos as atracoes
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao')
    filter_backends = [DjangoFilterBackend]

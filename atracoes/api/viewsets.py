from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    """
    Pego todos as atracoes
    E nela eu posso utilizar o filter ou o search
    Filter ele traz exatamente oque eu quero
    Search ele busca pelo oque eu quero
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'descricao')
    filter_backends = [DjangoFilterBackend]
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao']
    """
    '^': 'istartswith',
    '=': 'iexact',
    '@': 'search',
    '$': 'iregex',
    Para utilziar os prefixos busca colocar antes
    da variavel que está sendo utilizada exemplo:
    search_fields = ['^nome', '=descricao']
    """

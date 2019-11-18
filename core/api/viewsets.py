from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    Retorno todos os pontos turisticos
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer


class PontoTuristicoAprovadoViewSet(ModelViewSet):
    """
    Retorno so os pontos turisticos APROVADOS
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)


class PontoTuristicoViewSetNomeAlfabetico(ModelViewSet):
    """
    Retorno todos os pontos turisticos que contenha X no nome
    exemplo: http://127.0.0.1:8000/api/pontos-turisticos-nome/?nome=Ponto
    irá retornar todos os pontos que contém Ponto
    e irá colocalos em ordem alfabetica
    Caso não passe nada na variavel de ordenação irá retornar todos
    os pontos turisticos
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        nome = self.request.query_params.get('nome', None)

        if nome:
            queryset = PontoTuristico.objects.filter(nome__icontains=nome).order_by('nome')
            return queryset

        else:
            queryset = PontoTuristico.objects.all()
            return queryset

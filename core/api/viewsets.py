from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    Pego todos os pontos turisticos
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer


class PontoTuristicoAprovadoViewSet(ModelViewSet):
    """
    Pego so os pontos turisticos APROVADOS
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

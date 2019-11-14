from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet, PontoTuristicoAprovadoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'api/pontos-turisticos', PontoTuristicoViewSet)
router.register(r'api/pontos-turisticos-aprovados', PontoTuristicoAprovadoViewSet, base_name='PontoTuristico')
router.register(r'api/atracoes', AtracaoViewSet)
router.register(r'api/enderecos', EnderecoViewSet)
router.register(r'api/comentarios', ComentarioViewSet)
router.register(r'api/avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

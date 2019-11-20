from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto')


class PontoTuristicoSerializerCompleto(ModelSerializer):
    """
    Serializa todas as informações como objetos em vez de utlizar id
    IMPORTANTE: Para dar certo eles devem estar linkados no meu
    model PontoTuristico
    IMPORTANTE: o nome da minha variavel deve ser igual ao
    nome do field que será serializado
    """
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    enderecos = EnderecoSerializer(read_only=True)
    campo_customizado_no_serializer = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'campo_customizado_no_serializer', 'campo_customizado_no_model', 'nome', 'descricao',
            'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos'
                  )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            atrac = Atracao.objects.create(**atracao)
            ponto.atracoes.add(atrac)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        return ponto

    def get_campo_customizado_no_serializer(self, obj):
        return 'Nome: %s - Endereço: %s' % (obj.nome, obj.enderecos)

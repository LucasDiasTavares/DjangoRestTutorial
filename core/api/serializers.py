from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, CodigoIdentificacao
from atracoes.models import Atracao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer


class CodigoIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = CodigoIdentificacao
        fields = ('codigo', )


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
    enderecos = EnderecoSerializer()
    campo_customizado_no_serializer = SerializerMethodField()
    cod_identificacao = CodigoIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'campo_customizado_no_serializer', 'campo_customizado_no_model', 'nome', 'descricao',
            'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'enderecos', 'cod_identificacao'
                  )

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            atrac = Atracao.objects.create(**atracao)
            ponto.atracoes.add(atrac)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        enderecos = validated_data['enderecos']
        del validated_data['enderecos']
        end = Endereco.objects.create(**enderecos)

        codi = validated_data['cod_identificacao']
        del validated_data['cod_identificacao']
        codi = CodigoIdentificacao.objects.create(**codi)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        ponto.enderecos = end
        ponto.cod_identificacao = codi

        ponto.save()

        return ponto

    def get_campo_customizado_no_serializer(self, obj):
        return 'Nome: %s - Endereço: %s' % (obj.nome, obj.enderecos)

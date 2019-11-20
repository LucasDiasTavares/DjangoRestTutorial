from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco


class CodigoIdentificacao(models.Model):
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos-turisticos', null=True, blank=True)
    cod_identificacao = models.OneToOneField(
        CodigoIdentificacao, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def campo_customizado_no_model(self):
        return 'Nome: %s - Endereço: %s' % (self.nome, self.enderecos)

    def __str__(self):
        return self.nome

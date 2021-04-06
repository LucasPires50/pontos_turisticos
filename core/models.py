from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

# criando o model
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao) # acoplamento
    comentarios = models.ManyToManyField(Comentario) # acoplamento
    avaliacoes = models.ManyToManyField(Avaliacao) # acoplamento
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nome

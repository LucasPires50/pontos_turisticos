from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)# Mult-relacinamentos
    endereco = EnderecoSerializer()# Relacinamento Simples
    descricao_completa = serializers.SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
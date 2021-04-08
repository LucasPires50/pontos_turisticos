from django.contrib import admin
from .models import PontoTuristico
from .models import DocIdentificacao
from .actions import reprova_ponto_turistico, aprova_ponto_turistico


class PontoTuristicoAdmin(admin.ModelAdmin):
    # Mostar os campos na tela do django admin
    list_display=['nome', 'descricao', 'aprovado']

    actions = [reprova_ponto_turistico, aprova_ponto_turistico]

admin.site.register(PontoTuristico, PontoTuristicoAdmin)
admin.site.register(DocIdentificacao)


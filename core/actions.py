def reprova_ponto_turistico(modeladmin, request, queryset):
    queryset.update(aprovado=False)


def aprova_ponto_turistico(modeladmin, request, queryset):
    queryset.update(aprovado=True)

reprova_ponto_turistico.short_description = 'Reprovar ponto_turistico'
aprova_ponto_turistico.short_description = 'Aprovar ponto_turistico'
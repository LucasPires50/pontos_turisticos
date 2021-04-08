from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentarios, aprova_comentarios

# Implementar ao class actions admin do comentatios
class ComentatioAdmin(admin.ModelAdmin):
    # Mostar os campos na tela do django admin
    list_display=['usuario', 'data', 'aprovado']
    # Mostra as actons
    actions = [reprova_comentarios, aprova_comentarios]

admin.site.register(Comentario, ComentatioAdmin)
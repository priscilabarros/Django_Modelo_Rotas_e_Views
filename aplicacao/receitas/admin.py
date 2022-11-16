from django.contrib import admin
from .models import Receita

class ListandoReceitas( admin.ModelAdmin):
    list_display = ('id','nome_receita', 'categoria', 'tempo_preparo')
    list_display_links = ('id', 'nome_receita')
admin.site.register(Receita,ListandoReceitas)


from django.contrib import admin
from futebol.models import Clube, Jogador
from basicos.models import Cidade
from django.utils.html import format_html


class JogadorInline(admin.TabularInline):
  model = Jogador
  fields = ('foto_img', 'nome', 'numero_camisa', 'foto')
  readonly_fields = ('foto_img',)
  extra = 0

  @admin.display(description='Foto')
  def foto_img(self, obj):
    url = 'https://placehold.co/60'
    if (obj.foto):
      url = obj.foto.url
    
    return format_html(f'<img src="{url}" width="60" />')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
  search_fields = ['nome']


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
  list_display = ['escudo_img', 'nome', 'cidade', 'ano_fundacao', 'divisao', 'ver_detalhes']
  list_display_links = ['nome', 'ver_detalhes']
  autocomplete_fields = ['cidade']
  list_filter = ['divisao']
  search_fields = ['nome', 'cidade__nome']
  
  inlines = [JogadorInline]


  @admin.display(description='Escudo')
  def escudo_img(self, obj):
    url = 'https://placehold.co/60'
    if (obj.escudo):
      url = obj.escudo.url
    
    return format_html(f'<img src="{url}" width="60" />')

  def ver_detalhes(self, obj):
    return format_html("<p style='color: blue'>Ver Detalhes</p>")

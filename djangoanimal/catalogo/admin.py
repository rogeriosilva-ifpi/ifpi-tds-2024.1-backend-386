from django.contrib import admin
from catalogo.models import Produto
from django.utils.html import format_html



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['foto_produto', 'nome', 'detalhes', 'preco', 'disponivel']
  list_display_links = ['nome']
  list_filter = ('disponivel',)
  search_fields = ('nome', 'detalhes')
  actions = ['desabilitar_todos', 'habilitar_todos']

  @admin.action(description='Desabilitar Produtos')
  def desabilitar_todos(modeladmin, request, queryset):
    queryset.update(disponivel=False)

  @admin.action(description='Habilitar Produtos')
  def habilitar_todos(modeladmin, request, queryset):
    queryset.update(disponivel=True)

  def foto_produto(self, obj):
    url = 'https://placehold.co/80'
    
    if obj.foto:
      url = obj.foto.url
    
    return format_html(f'<img src={url} width=80 />')

  


# admin.site.register(Produto, ProdutoAdmin)
from django.contrib import admin
from catalogo.models import Produto




@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'detalhes', 'preco', 'disponivel']
  list_filter = ('disponivel',)
  search_fields = ('nome', 'detalhes')
  actions = ['desabilitar_todos', 'habilitar_todos']

  @admin.action(description='Desabilitar Produtos')
  def desabilitar_todos(modxxeladmin, request, queryset):
    queryset.update(disponivel=False)

  @admin.action(description='Habilitar Produtos')
  def habilitar_todos(modeladmin, request, queryset):
    queryset.update(disponivel=True)

  


# admin.site.register(Produto, ProdutoAdmin)
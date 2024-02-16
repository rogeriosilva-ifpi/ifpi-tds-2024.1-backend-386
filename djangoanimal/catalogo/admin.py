from django.contrib import admin

from catalogo.models import Produto


class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'detalhes', 'preco', 'disponivel']
  list_filter = ('disponivel',)
  search_fields = ('nome', 'detalhes')


admin.site.register(Produto, ProdutoAdmin)
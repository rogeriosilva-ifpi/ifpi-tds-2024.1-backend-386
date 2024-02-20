from django.contrib import admin

from catalogo.models import Produto, Categoria, Tag

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
  list_display = ['nome']
  search_fields = ['nome']


class TagInlineAdmin(admin.TabularInline):
  model = Tag
  extra = 0


class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'detalhes', 'preco', 'categoria', 'disponivel']
  list_filter = ('disponivel',)
  search_fields = ('nome', 'detalhes')

  autocomplete_fields = ['categoria']
  inlines = [TagInlineAdmin]


admin.site.register(Produto, ProdutoAdmin)
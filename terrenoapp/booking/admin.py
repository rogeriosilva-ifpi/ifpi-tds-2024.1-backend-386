from django.contrib import admin
from booking.models import Lote

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
  list_display = ['localizacao', 'area', 'valor']

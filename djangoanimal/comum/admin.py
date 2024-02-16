from django.contrib import admin

from comum.models import Animal

class AnimalAdmin(admin.ModelAdmin):
  list_display = ['nome', 'raca', 'ano']

admin.site.register(Animal, AnimalAdmin)

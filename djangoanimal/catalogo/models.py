from django.db import models

class Produto(models.Model):
  nome = models.CharField(max_length=120, null=False, 
        blank=False, verbose_name='Descrição')
  detalhes = models.CharField(max_length=1000, blank=True, null=True)
  preco = models.DecimalField(max_digits=6, decimal_places=2)
  disponivel = models.BooleanField(default=False)
  foto = models.ImageField(upload_to='imagens_produtos', null=True, blank=True)
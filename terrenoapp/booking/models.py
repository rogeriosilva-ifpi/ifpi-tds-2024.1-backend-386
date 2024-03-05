from django.db import models


class Lote(models.Model):
  area = models.PositiveIntegerField(null=False, blank=False)
  valor = models.DecimalField(max_digits=8, decimal_places=2)
  localizacao = models.CharField(max_length=250)

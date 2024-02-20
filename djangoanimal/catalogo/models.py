from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=120)

  def __str__(self):
    return self.nome


class Produto(models.Model):
  nome = models.CharField(max_length=120, null=False, 
        blank=False, verbose_name='Descrição')
  detalhes = models.CharField(max_length=1000, blank=True, null=True)
  preco = models.DecimalField(max_digits=6, decimal_places=2)
  disponivel = models.BooleanField(default=False)

  # relacionamentos
  categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='produtos', null=True)


class Tag(models.Model):
  nome = models.CharField(max_length=32)

  # relacionamentos
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='tags')

  
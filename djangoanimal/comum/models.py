from django.db import models

class Animal(models.Model):
  nome = models.CharField(null=False, blank=False, max_length=100)
  ano = models.IntegerField(default=2000)
  raca = models.CharField(max_length=60, default='Raça não Identificada')

  def __str__(self):
    return self.nome

  @property
  def idade(self):
    return 2024 - self.ano
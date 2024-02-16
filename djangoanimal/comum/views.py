from django.shortcuts import render
from django.http import HttpResponse
from comum.models import Animal

def lista_animais(request):
  animais = Animal.objects.all()

  lista = []

  for animal in animais:
    if animal.idade >= 10:
      lista.append(animal)
  
  context = {
    'animais': lista
  }

  return render(request, 'comum/animais.html', context)


def saudacao(request):
  return HttpResponse(content='Olá Breno, boa noite!')


def login(request):
  return render(request, 'comum/login.html')


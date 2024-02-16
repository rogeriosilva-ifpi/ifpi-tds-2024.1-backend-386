from django.urls import path
from comum import views

urlpatterns = [
  path('animais', views.lista_animais),
  path('boas-vindas', views.saudacao),
  path('login', views.login)
]
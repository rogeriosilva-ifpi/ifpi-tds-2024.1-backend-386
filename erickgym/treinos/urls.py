from django.urls import path
from treinos.views import (
    ListarCriarExerciciosView,
    DetalharAtualizarRemoverExercicioView)


urlpatterns = [
    path('api/exercicios', ListarCriarExerciciosView.as_view()),
    path('api/exercicios/<int:pk>', DetalharAtualizarRemoverExercicioView.as_view())
]

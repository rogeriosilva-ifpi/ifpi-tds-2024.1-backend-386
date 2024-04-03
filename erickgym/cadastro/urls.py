from django.urls import path
from .views import (
    ListarCriarAlunoView,
    DetalharAtualizarRemoverAlunoView,
    ListarCriarProfessorView,
    DetalharAtualizarRemoverProfessorView)


urlpatterns = [
    path('api/alunos', ListarCriarAlunoView.as_view()),
    path('api/alunos/<int:pk>', DetalharAtualizarRemoverAlunoView.as_view()),
    path('api/professores', ListarCriarProfessorView.as_view()),
    path('api/professores/<int:pk>',
         DetalharAtualizarRemoverProfessorView.as_view())
]

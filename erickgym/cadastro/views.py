from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import AlunoSerializer, ProfessorSerializer
from .models import Aluno, Professor


class ListarCriarAlunoView(ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class DetalharAtualizarRemoverAlunoView(RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class ListarCriarProfessorView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class DetalharAtualizarRemoverProfessorView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

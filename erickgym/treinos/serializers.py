from rest_framework.serializers import ModelSerializer
from treinos.models import Exercicio


class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'descricao',
                  'em_equipamento', 'idade_minima_aluno']

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from treinos.serializers import ExercicioSerializer
from treinos.models import Exercicio
from django.http import Http404


# CBV --> Class Based View
class ListarCriarExerciciosView(APIView):

    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalharAtualizarRemoverExercicioView(APIView):

    def get_object(self, pk):
        try:
            exercicio = Exercicio.objects.get(pk=pk)
            return exercicio
        except Exercicio.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        exercicio = self.get_object(pk)
        serializer = ExercicioSerializer(instance=exercicio)
        return Response(data=serializer.data)

    def put(self, request, pk):
        exercicio = self.get_object(pk)
        data = request.data
        serializer = ExercicioSerializer(instance=exercicio, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, pk):
        exercicio = self.get_object(pk)
        exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

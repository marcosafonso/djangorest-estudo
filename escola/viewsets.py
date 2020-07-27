from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from escola.models import Aluno, Disciplina, AlunoAtividade
from escola.serializers import AlunoSerializer, DisciplinaSerializer


class AlunoViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    # permission_classes = (IsAuthenticated,)

    # authentication_classes = (TokenAuthentication)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    """Sobrescrita no método para Delete, pois preciso excluir os 'inlines' de aluno-atividade, antes de excluir
       o próprio aluno"""
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # exclui primeiro as atividades do aluno:
        AlunoAtividade.objects.filter(aluno=instance).delete()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class DisciplinaViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


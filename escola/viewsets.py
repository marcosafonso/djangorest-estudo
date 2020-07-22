from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from escola.models import Aluno, Disciplina
from escola.serializers import AlunoSerializer, DisciplinaSerializer


class AlunoViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    # permission_classes = (IsAuthenticated,)

    # authentication_classes = (TokenAuthentication)
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class DisciplinaViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


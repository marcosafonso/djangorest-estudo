from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from demoapp.models import Location, Produto, ProdutoFornecedor
from demoapp.serializers import LocationSerializer, ProdutoSerializer, ProdutoFornecedorSerializer


class LocationViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    authentication_classes = (TokenAuthentication, )
    permission_classes = (DjangoModelPermissions,)


    """
        deixar de busca default por id na url: lookup_field.
    """
    # lookup_field = 'title'

    """
        django filter fields permite filtrar os registros. Sem a necessidade de criar manualmente:
    """
    # filter_fields = ('reference', 'title')

    """
        search_fields pode usar esses char especials:
        lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '@': 'search',
        '$': 'iregex',
    }
    """
    filter_backends = (SearchFilter,)
    search_fields = ('reference', 'title')


    # sobreescrita dos metodos desta modelviewset:

    # def get_queryset(self):

    # def list(self, request, *args, **kwargs):

    # def create(self, request, *args, **kwargs):

    # def destroy(self, request, *args, **kwargs):
    """
    Posso fazer log de delete aqui dentro.
    """

    # def retrieve(self, request, *args, **kwargs):
    #     pass
    """
       Pode-se checar quem tá acessando tal registro.
    """

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    """
        Pode-se criar actions personalizadas, sem ter que fazer url para isso:
        essa funciona com os methods definido no decorator. O parametro detail é afim de passar a pk.
    """
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'msg': 'denunciado'})


class ProdutoViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    #permission_classes = (IsAuthenticated,)

    """
    Token Authentication: para chamar o metodo tendo authenticacao por token, veja esse exemplo:
        curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
        
        - Veja que a chave que estará no header http é Authorization e a string começa com 'Token <seuTokenUser>'
    """
    # authentication_classes = (TokenAuthentication)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ProdutoFornecedorViewSet(ModelViewSet):
    """ ModelViewSet faz um crud completo, create, update, get list, delete"""
    queryset = ProdutoFornecedor.objects.all()
    serializer_class = ProdutoFornecedorSerializer


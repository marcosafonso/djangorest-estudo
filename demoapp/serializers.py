from rest_framework import serializers

from demoapp.models import Location, Family, Product, Transaction, Produto, ProdutoFornecedor


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'reference', 'title', 'description')


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('reference', 'title', 'description','unit','minQuantity')


class ProductSerializer(serializers.ModelSerializer):

    location = LocationSerializer()
    family = FamilySerializer()

    class Meta:
        model = Product
        fields = ('sku','barcode', 'title', 'description','location','family')
        depth = 1 # profundidade dos objects related


class TransactionSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Transaction
        fields = ('sku', 'barcode', 'product')


class ProdutoFornecedorSerializer(serializers.ModelSerializer):

    """ Fundamental ter o id aqui para fazer update ao usar como nested objects (entenda formset) em
    um cadastro Pai (nesse caso, cadastro de Produto)."""
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProdutoFornecedor
        fields = ('id', 'fornecedor',)


class ProdutoSerializer(serializers.ModelSerializer):

    """o campo fornecedores m2m aqui funciona como o antigo formset, permitindo salvar o produto, e juntamente
    seus fornecedores no mesmo cadastro.

    source é necessario para buscar os objetos relacionados no modo list (get).
    many=True é necessário para enviar vários (m2m isso é fundamental)
    """
    fornecedores = ProdutoFornecedorSerializer(source='produtofornecedor_set',
        many=True, read_only=False)

    class Meta:
        model = Produto
        fields = ('id', 'codigo', 'nome', 'fornecedores')

    """Funcao feita para criar os fornecedores do Produto"""
    def cria_fornecedores(self, fornecedores, produto):
        for fornecedor in fornecedores:
            fornec = ProdutoFornecedor.objects.create(**fornecedor, produto=produto)
            produto.fornecedores.add(fornec)

    """ Criar metodo que simular formset com o cadastro de produto """
    def create(self, validated_data):
        print(validated_data)
        fornecedores = validated_data['produtofornecedor_set']
        del validated_data['produtofornecedor_set']

        produto = Produto.objects.create(**validated_data)

        self.cria_fornecedores(fornecedores, produto)
        # for fornecedor in fornecedores:
        #     ProdutoFornecedor.objects.create(**fornecedor, produto=produto)

        return produto

    """ Método que atualiza o prodduto, e seus respectivos fornecedores.
        Atualiza, quando tem o id, quando não, cria um novo fornecedor para aquele produto."""
    def update(self, instance, validated_data):
        fornecedores = validated_data['produtofornecedor_set']
        del validated_data['produtofornecedor_set']

        instance = super().update(instance, validated_data)

        for fornece in fornecedores:
            fornece_id = fornece.get('id', None)

            if fornece_id:
                fornece_obj = ProdutoFornecedor.objects.get(id=fornece_id, produto=instance)
                fornece_obj.fornecedor = fornece.get('fornecedor', fornece_obj.fornecedor)
                fornece_obj.save()
            else:
                ProdutoFornecedor.objects.create(produto=instance, **fornece)

        return instance

        # print(validated_data)
        # fornecedores = validated_data['produtofornecedor_set']
        # del validated_data['produtofornecedor_set']
        #
        # instance = super().update(instance, validated_data)
        #
        # print(fornecedores)
        # # for fornecedor in fornecedores:
        # #     print(fornecedor)
        #     # fornec_obj = ProdutoFornecedor.objects.get(pk=int(fornecedor.get('id')))
        #     # fornec_obj.fornecedor = fornecedor.get('fornecedor')
        #
        #     # instance.fornecedores.add(fornec_obj)
        #
        # return instance




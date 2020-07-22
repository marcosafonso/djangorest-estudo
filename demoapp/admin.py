from django.contrib import admin

# Register your models here.
from demoapp.models import Product, Family, Location, Produto, ProdutoFornecedor

admin.site.register(Product)
admin.site.register(Family)

admin.site.register(Location)

admin.site.register(Produto)
admin.site.register(ProdutoFornecedor)

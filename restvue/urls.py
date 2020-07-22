"""restvue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from demoapp import views
from demoapp.views import home
from demoapp.viewsets import LocationViewSet, ProdutoViewSet, ProdutoFornecedorViewSet

#rotas da api:
from escola.viewsets import AlunoViewSet, DisciplinaViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'produtos_fornecedores', ProdutoFornecedorViewSet)

router.register(r'alunos', AlunoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)

urlpatterns = [
    #rest :
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),


    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #urls da api:
    path('products/', views.product_list, name='products'),
    path('products/<pk>', views.product_detail),
    path('families/', views.family_list.as_view()),
    path('families/<pk>)', views.family_detail.as_view()),
    # path('locations/', views.location_list.as_view(), name='locations'),
    # path('locations/<pk>)', views.location_detail.as_view()),
    path('transactions/', views.transaction_list.as_view()),
    path('transactions/<pk>', views.transaction_detail.as_view()),
]

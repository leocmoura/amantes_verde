from django.urls import path

from .views import CadastrarProdutoView

app_name = 'produto'

urlpatterns = [
    path('cadastrar/', CadastrarProdutoView.as_view(), name='cadastrar_produto'),
]
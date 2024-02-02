from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Produto
from .serializers import ProdutoSerializer


class CadastrarProdutoView(CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

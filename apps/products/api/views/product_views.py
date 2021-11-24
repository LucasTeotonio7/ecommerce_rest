from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        print(serializer)
        if serializer.is_valid():
            print("entrou aqui no is valid")
            serializer.save()
            return Response({'message': 'Produto criado corretamente!'},
                status=status.HTTP_201_CREATED)
        print("Não entrou no is valid")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
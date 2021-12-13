from rest_framework import viewsets
from rest_framework.response import Response
from apps.products.models import MeasureUnit

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers \
    import (MeasureUnitSerializer, CategoryProductSerializer,
            IndicatorSerializer)


class MeasureUnitListAPIView(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
            Retorna todas as unidades de medida do produto

            params.

            id -> PK da unidade de medida
            name -> nome da unidade de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)



class CategoryProductListAPIView(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
            Retorna todas as categorias de produto
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)


class IndicatorListAPIView(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
            Retorna todos os indicadores de produto
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)

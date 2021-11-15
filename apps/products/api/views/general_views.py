from rest_framework import generics

from apps.products.models import MeasureUnit, CategoryProduct, Indicator
from apps.products.api.serializers.general_serializers \
    import (MeasureUnitSerializer, CategoryProductSerializer,
            IndicatorSerializer)

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)


class CategoryProductListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state = True)


class IndicatorListAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return Indicator.objects.filter(state = True)

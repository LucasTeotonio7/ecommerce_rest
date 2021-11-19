from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers \
    import (MeasureUnitSerializer, CategoryProductSerializer,
            IndicatorSerializer)


class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

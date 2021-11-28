from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers \
    import (MeasureUnitSerializer, CategoryProductSerializer,
            IndicatorSerializer)


class ProductSerializer(serializers.ModelSerializer):
    # TODO: < METHOD 1 > --> calling the serializer
    # measure_unit = MeasureUnitSerializer()
    # category_product = CategoryProductSerializer()

    # TODO: < METHOD 2 > --> calling '__str__' from element
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')

    # TODO: < METHOD 3 > --> implementing the 'to_representation'
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else '',
        }
from django.urls import path

from apps.products.api.views.general_views \
    import (MeasureUnitListAPIView, CategoryProductListAPIView,
            IndicatorListAPIView)
from apps.products.api.views.product_views \
    import ProductListCreateAPIView, ProductRetrieveAPIView, \
        ProductDestroyAPIView, ProductUpdateAPIView


urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('product/retrieve/<int:pk>', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>', ProductDestroyAPIView.as_view(), name='product_destroy'),
    path('product/update/<int:pk>', ProductUpdateAPIView.as_view(), name='product_update'),
]

from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProductViewSet
from apps.products.api.views.general_views import *

router = DefaultRouter()

router.register(r'products',ProductViewSet, basename='Products')
router.register(r'measure-unit',MeasureUnitListAPIView, basename='measure_unit')
router.register(r'indicators',CategoryProductListAPIView, basename='indicators')
router.register(r'category-products',IndicatorListAPIView, basename='category_products')

urlpatterns = router.urls

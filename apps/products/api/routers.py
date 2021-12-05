from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'products',ProductViewSet, basename='Products')

urlpatterns = router.urls
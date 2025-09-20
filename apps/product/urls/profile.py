from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.product.views.profile import CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register("category", CategoryViewSet)
router.register("product", ProductViewSet)

urlpatterns = router.urls



from django_elasticsearch_dsl.search import Search
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.permissions import IsAuthenticated

from apps.product.models import Product, Category
from apps.product.serializers.profile import (CategorySerializerForPost, CategorySerializerForPatch,
                                              ProductSerializerForPost, ProductSerializerForPatch)
from apps.product.serializers.product import CategorySerializerForGet, ProductSerializerForGet
from apps.product.filters import ProductFilter
from apps.globals.permissions import IsOwner


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    parser_classes = (MultiPartParser, FormParser)
    queryset = Category.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).select_related("user")

    def get_serializer_class(self):
        serializer_classes = {
            "list": CategorySerializerForPost,
            "create": CategorySerializerForPost,
            "partial_update": CategorySerializerForPatch,
            "retrieve": CategorySerializerForPatch,
            "destroy": CategorySerializerForGet,
        }
        return serializer_classes.get(self.action, CategorySerializerForPost)


class ProductViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    filterset_class = ProductFilter
    http_method_names = ["get", "post", "patch", "delete"]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="search",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Search query",
            ),
            openapi.Parameter(
                name="category",
                in_=openapi.IN_QUERY,
                type=openapi.FORMAT_UUID,
                description='Category id',
            ),
            openapi.Parameter(
                name="price__gte",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_NUMBER,
                description="Price Greater Than or Equal To",
            ),
            openapi.Parameter(
                name="price__lte",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_NUMBER,
                description="Price Less Than or Equal To",
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.query_params.get("search")
        if not query:
            return Product.objects.filter(user=self.request.user).select_related("category", "user")

        s = Search(index="products").query(
            "multi_match",
            query=query,
            fields=["title^2", "description"],
            type="phrase_prefix"
        )
        response = s.execute()

        ids = [hit.id for hit in response]
        return Product.objects.filter(id__in=ids, user=self.request.user).select_related("category", "user")

    def get_serializer_class(self):
        serializer_classes = {
            "list": ProductSerializerForGet,
            "create": ProductSerializerForPost,
            "partial_update": ProductSerializerForPatch,
            "retrieve": ProductSerializerForPatch,
            "destroy": ProductSerializerForGet,
        }
        return serializer_classes.get(self.action, ProductSerializerForGet)




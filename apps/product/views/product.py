from django_elasticsearch_dsl.search import Search
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.product.models import Product, Category
from apps.product.serializers.product import ProductSerializerForGet, CategorySerializerForGet
from apps.product.filters import ProductFilter


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().select_related("category", "user")
    serializer_class = ProductSerializerForGet
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend]

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
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
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
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.query_params.get("search")
        if not query:
            return Product.objects.all()

        s = Search(index="products").query(
            "multi_match",
            query=query,
            fields=["title^2", "description"],
            type="phrase_prefix"
        )
        response = s.execute()

        ids = [hit.id for hit in response]
        return Product.objects.filter(id__in=ids)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().select_related("user")
    serializer_class = CategorySerializerForGet
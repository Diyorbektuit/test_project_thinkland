from rest_framework import serializers

from apps.product.models import Product, Category
from apps.user.serializer.profile import ProfileSerializer


class CategorySerializerForGet(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "description",
            "user"
        )


class ProductSerializerForGet(serializers.ModelSerializer):
    category = CategorySerializerForGet()
    user = ProfileSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "description",
            "price",
            "category",
            "user",
            "image",
            "created_at",
            "updated_at",
        )

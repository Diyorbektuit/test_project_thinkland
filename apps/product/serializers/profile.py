from rest_framework import serializers

from apps.product.models import Product, Category


class CategorySerializerForPostPatch(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "description"
        )

    def create(self, validated_data):
        user = self.context["request"].user
        return Category.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProductSerializerForPostPatch(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "image",
            "description",
            "price",
            "category"
        )

    def validate(self, attrs):
        if attrs.get("category") and attrs["category"].user != self.context["request"].user:
            raise serializers.ValidationError(detail={"category": "You are not the owner of this category"})
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        return Product.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

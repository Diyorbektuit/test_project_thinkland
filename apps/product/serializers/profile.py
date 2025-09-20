from rest_framework import serializers

from apps.product.models import Product, Category


class CategorySerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "description"
        )

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class CategorySerializerForPatch(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "image",
            "description"
        )

        extra_kwargs = {
            "title": {"required": False},
            "image": {"required": False},
            "description": {"required": False},
        }

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ProductSerializerForPost(serializers.ModelSerializer):
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
        if attrs["category"].user != self.context["request"].user:
            raise serializers.ValidationError(detail={"category": "You are not the owner of this category"})
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        return Product.objects.create(user=user, **validated_data)


class ProductSerializerForPatch(serializers.ModelSerializer):
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

        extra_kwargs = {
            "title": {"required": False},
            "image": {"required": False},
            "description": {"required": False},
            "price": {"required": False},
            "category": {"required": False},
        }

    def validate(self, attrs):
        if attrs.get("category") and attrs["category"].user != self.context["request"].user:
            raise serializers.ValidationError(detail={"category": "You are not the owner of this category"})
        return attrs

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


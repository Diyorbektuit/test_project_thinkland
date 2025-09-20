from rest_framework import serializers

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(detail={"password": "Passwords do not match"})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(detail={"username": "User with this username already exists"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        return {
            "username": instance.username,
            "access": str(RefreshToken.for_user(instance).access_token),
            "refresh": str(RefreshToken.for_user(instance)),
        }



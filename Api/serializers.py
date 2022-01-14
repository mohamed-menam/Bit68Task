from asyncio.format_helpers import extract_stack
import email
from unicodedata import name
from rest_framework import serializers


from Api.models import User, Product
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    @staticmethod
    def validate_login(data):
        if "email" not in data:
            raise serializers.ValidationError(
                {
                    "email": "Email is required!",
                }
            )

        if "password" not in data:
            raise serializers.ValidationError(
                {
                    "password": "Password is required!",
                }
            )

        return True


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

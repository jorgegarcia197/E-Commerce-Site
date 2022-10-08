from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # The model that we want to serialize
        model = Product
        # the fields that we want to serialize
        fields = "__all__"

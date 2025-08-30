from rest_framework import serializers
from .models import Order, OrderItem
from catalog.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "price", "total_price"]
        read_only_fields = ["price", "total_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ["id", "user", "status", "items", "total_price", "created_at", "updated_at"]
        read_only_fields = ["user", "status", "total_price", "created_at", "updated_at"]

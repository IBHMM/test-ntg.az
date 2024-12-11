from rest_framework import serializers


# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity']


# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'created_at', 'updated_at', 'items']

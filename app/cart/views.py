from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# class CartItemCreateAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CartItemSerializer

#     def get(self, request):
#         user = request.user
#         try:
#             cart = Cart.objects.get(user=user)
#             serializer = CartSerializer(cart)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Cart.DoesNotExist:
#             return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

#     def post(self, request):
#         cart = Cart.objects.get_or_create(user=request.user)[0]
#         serializer = CartItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(cart=cart)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CartItemUpdateAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CartItemSerializer

#     def put(self, request, pk):
#         try:
#             cart_item = CartItem.objects.get(pk=pk)
#         except CartItem.DoesNotExist:
#             return Response({'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = CartItemSerializer(cart_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             cart_item = CartItem.objects.get(pk=pk)
#         except CartItem.DoesNotExist:
#             return Response({'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

#         cart_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CartCheckoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         total = 0
#         try:
#             cart = Cart.objects.get(user=user)
#             cart_items = cart.items.all()
#             for item in cart_items:
#                 if item.quantity > item.product.stock:
#                     return Response({'message': f'Product {item.product.name} has insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)
#                 total += item.product.discounted_price() * item.quantity

#             for item in cart_items:
#                 item.product.stock -= item.quantity
#                 item.product.save()

#             cart_items.delete()

#             return Response({'message': f'Checkout successful. Total amount charged: {total}'}, status=status.HTTP_200_OK)
#         except Cart.DoesNotExist:
#             return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

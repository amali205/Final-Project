from .serilalizers import AddCartItemSerializer, CreateOrderSerializer,CartItemSerializer, ProductSerializer, CollectionSerializer, CustomerSerializer, OrderSerializer, CartSerializer
from rest_framework import viewsets , status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Product, Collection, Customer, Order, Cart, CartItem 
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin , DestroyModelMixin , RetrieveModelMixin ,ListModelMixin
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.permissions import IsAuthenticated , IsAdminUser 
from .permissions import IsAdminOrReadOnly




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title' , 'description']
    ordering_fields = ['price' , 'last_update']
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request, pk=None):
        # Correctly unpack get_or_create
        customer, created = Customer.objects.get_or_create(user=request.user)

        if request.method == 'GET':
            serializer = self.get_serializer(customer)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)




class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.annotate(products_count = Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
          
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer
    
    def get_serializer_context(self):
        return {'user_id': self.request.user.id}


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        # Get the customer's ID for the logged-in user
        customer = Customer.objects.only('id').get(user=user)
        return Order.objects.filter(customer_id=customer.id)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
  
   

class CartItemViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer   # for adding item
        return CartItemSerializer         # for listing items

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

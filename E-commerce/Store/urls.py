from django.urls import path ,include
from rest_framework.routers import DefaultRouter    
from .views import ProductViewSet, CollectionViewSet, CustomerViewSet ,OrderViewSet,  CartViewSet, CartItemViewSet 
from rest_framework_nested import routers


router = DefaultRouter()

router.register(r'products', ProductViewSet , basename='products')
router.register(r'customers', CustomerViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'carts', CartViewSet , basename='carts')
# router.register('items', CartItemViewSet, basename='cart-items')
router.register(r'orders', OrderViewSet , basename='orders')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + cart_router.urls
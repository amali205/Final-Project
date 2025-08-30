from django.urls import path
from .views import CartViewSet

cart_view = CartViewSet.as_view({
    "get": "list",
    "post": "add_item"
})

remove_view = CartViewSet.as_view({
    "delete": "remove_item"
})

urlpatterns = [
    path("", cart_view, name="cart"),
    path("remove/<int:pk>/", remove_view, name="cart-remove"),
]

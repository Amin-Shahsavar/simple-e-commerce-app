from django.urls import path, include
from rest_framework_nested import routers
from store import views


router = routers.DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('collection', views.CollectionViewSet, basename='collection')
router.register('cart', views.CartViewSet, basename='cart')
router.register('customer', views.CustomerViewSet, basename='customer')
router.register('order', views.OrderViewSet, basename='order')

product_review = routers.NestedDefaultRouter(router, 'product', lookup='product')
product_review.register('review', views.ReviewViewSet, basename='product-review')

cart_item = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
cart_item.register('item', views.CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_review.urls)),
    path('', include(cart_item.urls)),
]

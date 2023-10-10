from django.urls import path, include
from rest_framework_nested import routers
from store import views


router = routers.DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('collection', views.CollectionViewSet, basename='collection')
router.register('cart', views.CartViewSet, basename='cart')

product_review = routers.NestedDefaultRouter(router, 'product', lookup='product')
product_review.register('review', views.ReviewViewSet, basename='product-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_review.urls))
]

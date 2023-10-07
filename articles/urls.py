from django.urls import path, include
from rest_framework_nested import routers
from articles import views


router = routers.DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')
router.register('collection', views.CollectionViewSet)

article_router = routers.NestedDefaultRouter(router, 'article', lookup='article')
article_router.register('review', views.ReviewViewSet, basename='article-review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(article_router.urls)),
]

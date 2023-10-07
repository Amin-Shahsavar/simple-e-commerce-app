from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from articles.models import Article, Collection, Review
from articles.serializers import ArticleSerializer, CollectionSerializer, ReviewSerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['collection_id']
    search_fields = ['title', 'description']
    ordering_fields = ['published_at']
    
    # def delete(self, request, pk):
    #     article = get_object_or_404(Article, pk=pk)
    #     article.delete()
    #     return Response({'message': 'article successfuly deleted...'},
    #                     status=status.HTTP_204_NO_CONTENT)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        collection.delete()
        return Response({'message': 'collections successfuly deleted...'},
                        status=status.HTTP_204_NO_CONTENT)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(article_id=self.kwargs['article_pk'])

    def get_serializer_context(self):
        return {'article_id': self.kwargs['article_pk']}
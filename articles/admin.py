from django.contrib import admin
from articles.models import Article, Collection, Review


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'collection']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_article']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'description', 'date']

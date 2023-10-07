from django.contrib import admin
from articles.models import Article, Collection


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'collection']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured_article']

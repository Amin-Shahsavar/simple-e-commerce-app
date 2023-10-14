from django.db import models
from django.utils.translation import gettext_lazy as _
from authers.models import Auther


class Collection(models.Model):
    title = models.CharField(_("Title"), max_length=80, unique=True)
    featured_article = models.ForeignKey('Article', verbose_name=_(
        "Articles"), on_delete=models.SET_NULL, null=True, blank=True, related_name='+')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Article(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"), max_length=800)
    description = models.TextField(_("Description"), max_length=255)
    slug = models.SlugField(_("Slug"), default='-')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auther = models.ForeignKey(Auther, verbose_name=_(
        "Auther"), on_delete=models.PROTECT)
    collection = models.ForeignKey(Collection, verbose_name=_(
        "Collection"), on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Author(models.Model):
    pass


class Review(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

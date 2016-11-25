from random import randint
from django.db import models
from django.db.models.aggregates import Count
from django.utils import timezone


class ArticleManager(models.Manager):
    def random_article(self):
        # this is to show a random article as featured.
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]

    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(
            publication_date__lte=timezone.now())

    def unpublished_articles(self):
        return super(ArticleManager, self).get_queryset().filter(
            publication_date__gt=timezone.now())

    def every_article(self):
        return super(ArticleManager, self).get_queryset()

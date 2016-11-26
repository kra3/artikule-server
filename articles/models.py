from django.core.paginator import Paginator
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from .managers import ArticleManager


class Article(models.Model):
    SUGGESTIONS_COUNT = 4

    title = models.CharField(max_length=128)
    # at a later point, we could associate current logged in user as author.
    author = models.CharField(max_length=64)
    # allows future publication
    publication_date = models.DateTimeField()
    # populate them from another table as a choice field?
    category = models.CharField(max_length=64)
    # use some 3rd party module or write custom save method to generate thumbs
    hero_image = ThumbnailerImageField(upload_to="article/hero_imgs")
    opt_image = models.ImageField(upload_to="article/opt_imgs", null=True, blank=True)
    content = models.TextField()

    objects = ArticleManager()

    def __str__(self):
        return "<Article: {} - {}>".format(self.title, self.author)

    class Meta:
        ordering = ("-publication_date",)

    @classmethod
    def get_random_article(cls):
        return cls.objects.random_article()

    @classmethod
    def get_article_suggestions(cls, next_page=1):
        # I'm using a simple pagination over all the avialble articles
        # however in real life, we have to look for multiple scenarios
        # - avoid showing the same articles which is shown in the
        # same page in other sections.
        # - implement as a recomenndation system where we have to show
        # similar articles to currently displayed articles, also user's
        # taste will come into play.
        paginator = Paginator(cls.objects.all(), cls.SUGGESTIONS_COUNT)
        next_page = next_page if next_page in paginator.page_range else 1
        page = paginator.page(next_page)
        return {
            'total_pages': paginator.num_pages,
            'page_number': next_page,
            'articles': page.object_list
        }

    @property
    def as_json(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'author': self.author,
            'publication_date': self.publication_date,
            'category': self.category,
            'hero_image': self.hero_image.url,
            'opt_image': self.opt_image.url if self.opt_image else '',
            'content': self.content
        }

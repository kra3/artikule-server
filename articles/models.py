from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from .managers import ArticleManager


class Article(models.Model):
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

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    # at a later point, we could associate current logged in user as author.
    author = models.CharField(max_length=64)
    # allows future publication
    publication_date = models.DateTimeField()
    # populate them from another table as a choice field?
    category = models.CharField(max_length=64)
    # use some 3rd party module or write custom save method to generate thumbs
    hero_image = models.ImageField()
    opt_image = models.ImageField()
    content = models.TextField()
